from typing import List, Dict
from jinja2 import Template

from dftools.core.structure.core.structure import Structure
from dftools.core.structure.core.namespace import Namespace
from dftools.core.structure.compare import StructureComparisonResult
from dftools.core.structure.jinja import StructureJinjaDictEncoder, StructureComparedJinjaDictEncoder
from dftools.exceptions import MissingMandatoryArgumentException


class StructureChangeSQLGenerationApiAbstract:
    """
        Generates SQL for changes on the structure

        Cases are :
            - Structure Removed (Structure to be dropped)
            - Structure Created (Structure to be created from scratch)
            - Structure Updated (Structure to be updated with data to be kept)
    """

    def __init__(self
                 , allowed_structure_types: List[str] = ['BASE TABLE', 'VIEW']
                 , structure_jinja_dict_encoder : type = StructureJinjaDictEncoder
                 , structure_compared_jinja_dict_encoder : type = StructureComparedJinjaDictEncoder
                 , rendering_params : Dict[str, str] = {}) -> None:
        self.allowed_structure_types = allowed_structure_types
        self.structure_jinja_dict_encoder = structure_jinja_dict_encoder
        self.structure_compared_jinja_dict_encoder = structure_compared_jinja_dict_encoder
        self.namespace = None
        self.rendering_params = rendering_params if rendering_params is not None else {}

    def set_namespace(self,  namespace : Namespace) -> None:
        self.namespace = namespace

    def get_namespace(self) -> Namespace:
        return self.namespace

    def set_rendering_params(self,  rendering_params : Dict[str, str]) -> None:
        self.rendering_params = rendering_params

    def get_namespace(self) -> Dict[str, str]:
        return self.rendering_params

    def is_allowed(self, orig: Structure, new: Structure):
        if (orig is None) & (new is None):
            return False
        structure_type = orig.type if orig is not None else new.type
        if structure_type not in self.allowed_structure_types:
            return False
        return True

    def create_sql(self, structure_comparison: StructureComparisonResult) -> str:
        orig: Structure = structure_comparison.obj1
        new: Structure = structure_comparison.obj2
        key_path = structure_comparison.get_structure_level_key()
        if not self.is_allowed(orig, new):
            raise RuntimeError(f"Create SQL for Structure Change requires at least one structure as original or as "
                               f"new and should be of one of "
                               f"the allowed types : {','.join(self.allowed_structure_types)}")
        if structure_comparison.is_identical(root_key=[key_path[0]]):
            raise RuntimeError('Create SQL for Structure Change is applicable only for changes')

        if structure_comparison.is_removed(root_key=[key_path[0]]):
            return self._get_drop_structure_sql(orig)
        elif structure_comparison.is_new(root_key=[key_path[0]]):
            return self._get_create_structure_sql(new)
        return self._get_alter_structure_sql(structure_comparison)

    def _get_create_structure_sql(self, structure: Structure) -> str:
        return NotImplementedError(
            'The _get_create_structure_sql method is not implemented for class : ' + str(type(self)))

    def _get_alter_structure_sql(self, structure_comparison: StructureComparisonResult) -> str:
        return NotImplementedError(
            'The _get_alter_structure_sql method is not implemented for class : ' + str(type(self)))

    def _get_drop_structure_sql(self, structure: Structure) -> str:
        return NotImplementedError(
            'The _get_drop_structure_sql method is not implemented for class : ' + str(type(self)))


class StructureChangeSQLGenerationApi(StructureChangeSQLGenerationApiAbstract):

    def __init__(self
                 , allowed_structure_types: List[str] = ['BASE TABLE']
                 , structure_jinja_dict_encoder: type = StructureJinjaDictEncoder
                 , structure_compared_jinja_dict_encoder: type = StructureComparedJinjaDictEncoder
                 , create_structure_sql_template: Template = None
                 , drop_structure_sql_template: Template = None
                 , alter_structure_sql_template: Template = None
                 , rendering_params : Dict[str, str] = {}) -> None:
        super().__init__(allowed_structure_types, structure_jinja_dict_encoder, structure_compared_jinja_dict_encoder
                         , rendering_params)
        if create_structure_sql_template is None:
            raise MissingMandatoryArgumentException(method_name='Init'
                                                    , object_type=type(self),
                                                    argument_name='Create Structure SQL Template')
        if drop_structure_sql_template is None:
            raise MissingMandatoryArgumentException(method_name='Init'
                                                    , object_type=type(self),
                                                    argument_name='Drop Structure SQL Template')
        if alter_structure_sql_template is None:
            raise MissingMandatoryArgumentException(method_name='Init'
                                                    , object_type=type(self),
                                                    argument_name='Alter Structure SQL Template')
        self.create_structure_sql_template = create_structure_sql_template
        self.drop_structure_sql_template = drop_structure_sql_template
        self.alter_structure_sql_template = alter_structure_sql_template

    def _get_create_structure_sql(self, structure: Structure) -> str:
        return self.structure_jinja_dict_encoder.create_statement(
            self.create_structure_sql_template, self.namespace, structure, params=self.rendering_params)

    def _get_alter_structure_sql(self, structure_comparison: StructureComparisonResult) -> str:
        return self.structure_compared_jinja_dict_encoder.create_statement(
            self.alter_structure_sql_template, self.namespace, structure=structure_comparison.obj2
            , structure_comparison=structure_comparison, params=self.rendering_params)

    def _get_drop_structure_sql(self, structure: Structure) -> str:
        return self.structure_jinja_dict_encoder.create_statement(
            self.drop_structure_sql_template, self.namespace, structure, params=self.rendering_params)
