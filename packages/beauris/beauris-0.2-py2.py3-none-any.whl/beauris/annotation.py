import logging
import os

from .blastbank import BlastBank
from .expression_data import ExpressionData
from .managed_entity import ManagedEntity
from .managed_file import InputFile

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class Annotation(ManagedEntity):

    def __init__(self, config, yml_data, assembly):

        ManagedEntity.__init__(self, config, default_services=assembly.deploy_services, yml_data=yml_data)

        self.assembly = assembly

        self.version = self.yml_data['version']

        self.entity_name = 'annotation'

        self.input_files = {
            'gff': InputFile.from_yml(self.yml_data["file"], name='gff', version=self.version)
        }

        self.expressions = self._load_expressions()

        self.tasks = self.config.get_tasks(self)

        self.load_tasks_derived_files()

        self.blastbanks = [
            BlastBank(self, 'blastdb_cds', self.derived_files['cds_fa'], self.derived_files['blastdb_cds_nhr'], "annotation_cds", 'nucl'),
            BlastBank(self, 'blastdb_transcripts', self.derived_files['transcripts_fa'], self.derived_files['blastdb_transcripts_nhr'], "annotation_transcripts", 'nucl'),
            BlastBank(self, 'blastdb_proteins', self.derived_files['proteins_fa'], self.derived_files['blastdb_proteins_phr'], "annotation_proteins", 'prot')
        ]

    def get_blast_link(self, bank, server):

        # TODO add a link to GNB when ready

        link = '{id}'

        if bank.input_fasta.name in ('cds_fa', 'transcripts_fa'):
            # Annotation tracks are indexed, it should be possible to link to features directly
            if 'jbrowse' in self.get_deploy_services(server):
                link = '<a href="' + self.config.get_service_url('jbrowse', server, self.assembly.organism) + '?data=data%2F' + self.assembly.slug(short=True) + '&loc={id}">{id}</a>'

            if 'apollo' in self.get_deploy_services(server) and 'apollo' in self.config.raw and server in self.config.raw['apollo']:

                common_name = self.assembly.organism.pretty_name()
                common_name += " {}".format(self.assembly.version)
                common_name = common_name.replace(' ', '%20')

                link += ' <a href="{}annotator/loadLink?organism='.format(self.config.get_service_url('apollo', server)) + common_name + '&loc={id}">Apollo</a>'

        return link

    def slug(self, short=False):

        if short:
            return "{}_annot{}".format(self.assembly.slug(short), self.version)
        else:
            return "{}/annotation_{}".format(self.assembly.slug(short), self.version)

    def pretty_name(self, with_parent=True):

        if with_parent:
            return "{} annotation {}".format(self.assembly.pretty_name(), self.version)
        else:
            return "Annotation {}".format(self.version)

    def get_children(self):

        return self.expressions

    def get_organism(self):

        return self.assembly.organism

    def get_work_dir(self):

        return os.path.join(self.assembly.get_work_dir(), "annotation_{}".format(self.version))

    def get_locked_yml(self):

        locked_yml = self.yml_data

        locked_yml['file'] = self.input_files['gff'].to_yml()

        if self.expressions:
            locked_yml['expression_data'] = []

            for exp in self.expressions:
                locked_yml['expression_data'].append(exp.get_locked_yml())

        if len(self.derived_files):
            locked_yml['derived'] = []

            for id, der in self.derived_files.items():
                locked_yml['derived'].append(der.to_yml())

        return locked_yml

    def load_locked_data(self, locked_yml, future=False):

        ManagedEntity.load_locked_data(self, locked_yml, future)

        for exp in self.expressions:
            matching = exp.find_matching_yml_in_list(locked_yml.get("expression_data", []))
            if matching:
                exp.load_locked_data(matching, future)

        if 'file' in locked_yml:
            self.input_files['gff'].merge_with_locked(locked_yml["file"], future)

    def get_metadata(self, inherit=True):

        metadata = {'annotation_version': self.version}

        if inherit:
            metadata.update(self.assembly.get_metadata())

        metadata.update(self.get_basic_metadata())

        return metadata

    def _load_expressions(self):
        expressions = []
        for exp in self.yml_data.get("expression_data", []):
            expressions.append(ExpressionData(self.config, exp, self))

        return expressions
