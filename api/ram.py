import json
import logging
import os
from helpers.page_helpers import *
from helpers.datastore_helpers import *

################################################################################
# Setup helper functions
################################################################################

# N/A

################################################################################
# Setup routes
################################################################################

@route('/api/ram/register/resource-type', method='POST')
def api_register_resource_type():
    logging.debug("IN api_register_resource_type")
    # json_data = request.json
    # logging.info(str(json_data))
    # cwd = os.getcwd()
    # logging.info(cwd)
    # logging.info(str(dir(request)))
    # logging.info(request.is_ajax);
    # logging.info(request.is_xhr);
    # logging.info(request.content_type);
    # logging.info(request.json);
    # for key in request.json:
    #     logging.info("key [{0}] has value of {1}".format(key, request.json[key]))
    # key [count] has value of 1
    # key [des] has value of Conference room
    # key [name] has value of RM
    
    ########################################
    
    # User input assignment
    user_json = request.json
    type_name = user_json['name'] if "name" in user_json else None
    type_desc = user_json['des'] if "des" in user_json else None
    type_count = user_json['count'] if "count" in user_json else None
    type_code = user_json['code'] if "code" in user_json else None
    
    # User input validation; making sure we have all the required fields
    logging.info("type {0}".format(type_name))
    logging.info("type {0}".format(type_desc))
    logging.info("type {0}".format(type_count))
    logging.info("type {0}".format(type_code))

    # Save to database
    #db = get_mongodb("brahman") # db = client[db_name]
    ################################################################################
    try:
        db = get_mongodb('hci_admin')
        result = db.resource_types.insert_one({
            "name" : type_name,
            "description" : type_desc
        })
    except Exception as ex:
        logging.error(ex)

    logging.info("result:[{0}]".format(result))
    logging.info(str(dir(result)))
    # 
    op_result = {
        "success" : True,
        "message" : "OK"
    }
    return json.dumps(op_result)


@route('/api/ram/list/resource-type', method=['POST','GET'])
def api_list_resource_type():
    logging.debug("IN api_list_resource_type")
    # try:
    db = get_mongodb('hci_admin')
    logging.debug("step1")
    collection = []
    for rec in db.resource_types.find({}):
        collection.append({
            '_id' : str(rec['_id']),
            'count': rec['count'],
            'name': rec['name'],
            'desc': rec['desc']
        })
    return json.dumps(collection)

# @route('/api/sample')
# def api_sample_get():
#     logging.debug("IN api_sample_get")
#     return "['Hello', 'World']"
    