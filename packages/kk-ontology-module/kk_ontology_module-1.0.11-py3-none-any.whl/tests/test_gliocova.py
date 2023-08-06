from kk_ontology_module import CancerOntology
import pandas as pd

def test_gliocova():
    o = CancerOntology()
    data_points = {'PSEUDO_PATIENTID':[1021312],'PSEUDO_TUMOURID':[1241251],'SITE_ICD10_O2':['C445'],'BEHAVIOUR_ICD10_O2':[1],'MERGED_REGIMEN_ID':[11251],
                    'AGE':[51],'VITALSTATUS':['A'],'PRIMARY_DIAGNOSIS':['Aasdasasd'],'SEX':['M'],'DIAGNOSISYEAR':[1998],'BENCHMARK_GROUP':['Docetaxel']}
    o.set_gliocova_column_names()
    df = pd.DataFrame(data_points)
    o.define_data(df)
    o.reason()
    assert o.onto.Patient.instances() == [1]