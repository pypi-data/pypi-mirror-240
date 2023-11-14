###default __init__ 
__version__='1.0.0' 
 
from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

 

 
#from biopax.doc.rh_templatereactionregulation import rh_templatereactionregulation_DocHelper
 
#from biopax.doc.rh_entityreference import rh_entityreference_DocHelper
 
#from biopax.doc.rh_evidencecodevocabulary import rh_evidencecodevocabulary_DocHelper
 
#from biopax.doc.rh_proteinreference import rh_proteinreference_DocHelper
 
#from biopax.doc.rh_covalentbindingfeature import rh_covalentbindingfeature_DocHelper
 
#from biopax.doc.rh_sequenceregionvocabulary import rh_sequenceregionvocabulary_DocHelper
 
#from biopax.doc.rh_relationshipxref import rh_relationshipxref_DocHelper
 
#from biopax.doc.rh_protein import rh_protein_DocHelper
 
#from biopax.doc.rh_transportwithbiochemicalreaction import rh_transportwithbiochemicalreaction_DocHelper
 
#from biopax.doc.rh_rna import rh_rna_DocHelper
 
#from biopax.doc.rh_rnareference import rh_rnareference_DocHelper
 
#from biopax.doc.rh_cellvocabulary import rh_cellvocabulary_DocHelper
 
#from biopax.doc.rh_provenance import rh_provenance_DocHelper
 
#from biopax.doc.rh_evidence import rh_evidence_DocHelper
 
#from biopax.doc.rh_conversion import rh_conversion_DocHelper
 
#from biopax.doc.rh_physicalentity import rh_physicalentity_DocHelper
 
#from biopax.doc.rh_deltag import rh_deltag_DocHelper
 
#from biopax.doc.rh_interaction import rh_interaction_DocHelper
 
#from biopax.doc.rh_dnareference import rh_dnareference_DocHelper
 
#from biopax.doc.rh_biosource import rh_biosource_DocHelper
 
#from biopax.doc.rh_entityreferencetypevocabulary import rh_entityreferencetypevocabulary_DocHelper
 
#from biopax.doc.rh_xref import rh_xref_DocHelper
 
#from biopax.doc.rh_fragmentfeature import rh_fragmentfeature_DocHelper
 
#from biopax.doc.rh_relationshiptypevocabulary import rh_relationshiptypevocabulary_DocHelper
 
#from biopax.doc.rh_chemicalstructure import rh_chemicalstructure_DocHelper
 
#from biopax.doc.rh_experimentalformvocabulary import rh_experimentalformvocabulary_DocHelper
 
#from biopax.doc.rh_interactionvocabulary import rh_interactionvocabulary_DocHelper
 
#from biopax.doc.rh_degradation import rh_degradation_DocHelper
 
#from biopax.doc.rh_sequencemodificationvocabulary import rh_sequencemodificationvocabulary_DocHelper
 
#from biopax.doc.rh_templatereaction import rh_templatereaction_DocHelper
 
#from biopax.doc.rh_bindingfeature import rh_bindingfeature_DocHelper
 
#from biopax.doc.rh_pathway import rh_pathway_DocHelper
 
#from biopax.doc.rh_publicationxref import rh_publicationxref_DocHelper
 
#from biopax.doc.rh_modulation import rh_modulation_DocHelper
 
#from biopax.doc.rh_controlledvocabulary import rh_controlledvocabulary_DocHelper
 
#from biopax.doc.rh_sequenceinterval import rh_sequenceinterval_DocHelper
 
#from biopax.doc.rh_dnaregion import rh_dnaregion_DocHelper
 
#from biopax.doc.rh_sequencelocation import rh_sequencelocation_DocHelper
 
#from biopax.doc.rh_kprime import rh_kprime_DocHelper
 
#from biopax.doc.rh_biochemicalpathwaystep import rh_biochemicalpathwaystep_DocHelper
 
#from biopax.doc.rh_entityfeature import rh_entityfeature_DocHelper
 
#from biopax.doc.rh_smallmoleculereference import rh_smallmoleculereference_DocHelper
 
#from biopax.doc.rh_experimentalform import rh_experimentalform_DocHelper
 
#from biopax.doc.rh_pathwaystep import rh_pathwaystep_DocHelper
 
#from biopax.doc.rh_rnaregion import rh_rnaregion_DocHelper
 
#from biopax.doc.rh_rnaregionreference import rh_rnaregionreference_DocHelper
 
#from biopax.doc.rh_molecularinteraction import rh_molecularinteraction_DocHelper
 
#from biopax.doc.rh_tissuevocabulary import rh_tissuevocabulary_DocHelper
 
#from biopax.doc.rh_biochemicalreaction import rh_biochemicalreaction_DocHelper
 
#from biopax.doc.rh_complexassembly import rh_complexassembly_DocHelper
 
#from biopax.doc.rh_catalysis import rh_catalysis_DocHelper
 
#from biopax.doc.rh_control import rh_control_DocHelper
 
#from biopax.doc.rh_transport import rh_transport_DocHelper
 
#from biopax.doc.rh_modificationfeature import rh_modificationfeature_DocHelper
 
#from biopax.doc.rh_complex import rh_complex_DocHelper
 
#from biopax.doc.rh_cellularlocationvocabulary import rh_cellularlocationvocabulary_DocHelper
 
#from biopax.doc.rh_phenotypevocabulary import rh_phenotypevocabulary_DocHelper
 
#from biopax.doc.rh_score import rh_score_DocHelper
 
#from biopax.doc.rh_gene import rh_gene_DocHelper
 
#from biopax.doc.rh_stoichiometry import rh_stoichiometry_DocHelper
 
#from biopax.doc.rh_smallmolecule import rh_smallmolecule_DocHelper
 
#from biopax.doc.rh_dna import rh_dna_DocHelper
 
#from biopax.doc.rh_geneticinteraction import rh_geneticinteraction_DocHelper
 
#from biopax.doc.rh_unificationxref import rh_unificationxref_DocHelper
 
#from biopax.doc.rh_sequencesite import rh_sequencesite_DocHelper
 
#from biopax.doc.rh_dnaregionreference import rh_dnaregionreference_DocHelper
 
#from biopax.doc.rh_utilityclass import rh_utilityclass_DocHelper
 
#from biopax.doc.rh_entity import rh_entity_DocHelper
 
######## unexpected name: <N2aadcc1d61524d598330ae06e6d6d2c2> 
  


