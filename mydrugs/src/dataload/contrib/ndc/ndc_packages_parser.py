import csv

def restr_dict(dictionary):
    _d = {}
    _d['ndc'] = {}
    _d['ndc']['package'] = {}
    
    for key in dictionary:       
        if key == 'PRODUCTID':
            print dictionary[key]            
            _d.update({'_id':dictionary[key]})           
            _d['ndc'].update({'product_id':dictionary[key]})           
        elif key == 'NDCPACKAGECODE':
            _d['ndc']['package'].update({key.lower():dictionary[key]})
        elif key == 'PACKAGEDESCRIPTION':
            _d['ndc']['package'].update({key.lower():dictionary[key]})
        else:
            _d['ndc'].update({key.lower():dictionary[key]})
    return _d   
   
def csv_to_dict(_file):
    f = open(_file,'r')
    reader = csv.DictReader(f)
    for row in reader:        
        _dict = restr_dict(row)
        _dict = dict_sweep(_dict)
        yield _dict


    

