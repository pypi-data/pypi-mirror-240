##generated class BioSource
#############################
##   Definition: The biological source (organism, tissue or cell type) of an Entity.
##   Usage: Some entities are considered source-neutral (e.g. small molecules), and
##   the biological source of others can be deduced from their constituentss (e.g.
##   complex, pathway).  Instances: HeLa cells, Homo sapiens, and mouse liver tissue.

##############################
 
from biopax.utilityclass import UtilityClass
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class BioSource(UtilityClass) :
##########constructor
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        
        self.pk=kwargs.get('pk',None)    
        self.pop_state=kwargs.get('pop_state',None)  
        self.exhausted=kwargs.get('exhausted',None)
        self.meta_label=None  
        
        super().__init__(*args, **kwargs) 
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#BioSource"
##   A cell type, e.g. 'HeLa'. This should reference a term in a controlled
##   vocabulary of cell types. Best practice is to refer to OBO Cell Ontology.
##   http://www.obofoundry.org/cgi-bin/detail.cgi?id=cell

        self._cellType=kwargs.get('cellType',None)  
##   An external controlled vocabulary of tissue types.

        self._tissue=kwargs.get('tissue',None)  
##   Values of this property define external cross-references from this entity to
##   entities in external databases.

        self._xref=kwargs.get('xref',None)  
##   An abbreviated name for this entity, preferably a name that is short enough to
##   be used in a visualization application to label a graphical element that
##   represents this entity. If no short name is available, an xref may be used for
##   this purpose by the visualization application.  Warning:  Subproperties of name
##   are functional, that is we expect to have only one standardName and shortName
##   for a given entity. If a user decides to assign a different name to standardName
##   or shortName, they have to remove the old triplet from the model too. If the old
##   name should be retained as a synonym a regular "name" property should also be
##   introduced with the old name.

        self._displayName=kwargs.get('displayName',None)  
##   Synonyms for this entity.  standardName and shortName are subproperties of this
##   property and if declared they are automatically considered as names.   Warning:
##   Subproperties of name are functional, that is we expect to have only one
##   standardName and shortName for a given entity. If a user decides to assign a
##   different name to standardName or shortName, they have to remove the old triplet
##   from the model too. If the old name should be retained as a synonym a regular
##   "name" property should also be introduced with the old name.

        self._name=kwargs.get('name',None)  
##   The preferred full name for this entity, if exists assigned by a standard
##   nomenclature organization such as HUGO Gene Nomenclature Committee.  Warning:
##   Subproperties of name are functional, that is we expect to have only one
##   standardName and shortName for a given entity. If a user decides to assign a
##   different name to standardName or shortName, they have to remove the old triplet
##   from the model too. If the old name should be retained as a synonym a regular
##   "name" property should also be introduced with the old name.

        self._standardName=kwargs.get('standardName',None)  
  

##########getter
     
    def get_cellType(self):
        return self._cellType  
     
    def get_tissue(self):
        return self._tissue  
     
    def get_xref(self):
        return self._xref  
     
    def get_displayName(self):
        return self._displayName  
     
    def get_name(self):
        return self._name  
     
    def get_standardName(self):
        return self._standardName  
  
##########setter
    
    @validator(value='biopax.CellVocabulary')  
 
    def set_cellType(self,value):
        self._cellType=value  
    
    @validator(value='biopax.TissueVocabulary')  
 
    def set_tissue(self,value):
        self._tissue=value  
    
    @validator(value='biopax.Xref')  
 
    def set_xref(self,value):
        self._xref=value  
    
    @validator(value=str)  
 
    def set_displayName(self,value):
        self._displayName=value  
    
    @validator(value=str)  
 
    def set_name(self,value):
        self._name=value  
    
    @validator(value=str)  
 
    def set_standardName(self,value):
        self._standardName=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      satt=['cellType', 'tissue', 'xref']
      for elem in satt:
        object_attribute_list.append(elem)
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      satt=['displayName', 'name', 'standardName']
      for elem in satt:
        type_attribute_list.append(elem)
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['cellType']='CellVocabulary'  
      ma['tissue']='TissueVocabulary'  
      ma['xref']='Xref'  
      ma['displayName']='str'  
      ma['name']='str'  
      ma['standardName']='str'  
      return ma



    def to_json(self):
        return tojson(self)
        

