import unittest
from InCli import InCli
from InCli.SFAPI import account,restClient,CPQAppHandler,DR_IP,jsonFile

class Test_CPQUtils_Class(unittest.TestCase):
    def getcartNodes(self,cartItems,productCode,itemType=None):
        inp = {
            'cartItems':cartItems,
            'key':'ProductCode',
            'value':productCode
        }
        if itemType!=None:
            inp['itemType'] = itemType
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        return res

    def test_getcartNodes(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xGaJAAU'
        productCode = 'C_SIM_CARD'
        cartItems = CPQAppHandler.getCartsItems(orderId)

        inp = {
            'cartItems':cartItems,
            'key':'ProductCode',
            'value':productCode
        }
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        for r in res['cartNodes']:
            print(f"{r['ProductCode']}    {r['itemType']}")

        inp = {
            'cartItems':cartItems,
            'value':productCode
        }
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        for r in res['cartNodes']:
            print(f"{r['ProductCode']}    {r['itemType']}")

        print()

    def postCartItems(self,orderId,cartNodes):
        inp2 = {
            'orderId':orderId,
          #  'cartItems':cartItems,
          #  'value':productCode,
            'cartNodes':cartNodes
        }

        res=DR_IP.remoteClass('CPQUtils','postCartItems',inp2,{})
        return res

    def test_getHierarchy_and_postCartItems(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xGaJAAU'
        productCode = 'C_SIM_CARD'

        cartItems = CPQAppHandler.getCartsItems(orderId)

        inp = {
            'cartItems':cartItems,
            'value':productCode
        }
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        inp2 = {
            'orderId':orderId,
            'cartItems':cartItems,
            'value':productCode,
            'cartNodes':res['cartNodes']
        }

        res2=DR_IP.remoteClass('CPQUtils','postCartItems',inp2,{})

        print()

    def test_getHierarchy_and_getObject(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xGaJAAU'
        productCode = 'C_SIM_CARD'

        cartItems = CPQAppHandler.getCartsItems(orderId)

        inp = {
            'cartItems':cartItems,
            'value':productCode,
            'itemType':'lineItem'
        }
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        inp2 = {
            'key':'code',
            'value':'ATT_DELIVERY_METHOD',
            'object':res['cartNodes'][0]
        }

        res2=DR_IP.remoteClass('CPQUtils','getObject',inp2,{})

        print()
        res2['data']['userValues']

    def putCartItems(self,orderId,cartNodes,updateAttributeJSON=None,updateFieldsJSON=None):
        inp2 = {
            'orderId':orderId,
      #      'cartItems':cartItems,
      #      'value':productCode,
            'cartNodes':cartNodes
      #      'returnPayload':True,
        }  

        if updateAttributeJSON != None:
            inp2['updateAttributeJSON'] = updateAttributeJSON 
        if updateFieldsJSON != None:
            inp2['updateFieldsJSON'] = updateFieldsJSON 

        res2=DR_IP.remoteClass('CPQUtils','putCartsItems',inp2,{})
        return res2


    def test_getHierarchy_and_putCartItems(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xGaJAAU'
        productCode = 'C_SIM_CARD'

        cartItems = CPQAppHandler.getCartsItems(orderId)

        inp = {
            'cartItems':cartItems,
            'value':productCode,
            'itemType':'lineItem'

        }
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        inp2 = {
            'orderId':orderId,
      #      'cartItems':cartItems,
            'value':productCode,
            'cartNodes':res['cartNodes'],
      #      'returnPayload':True,
            'updateFieldsJSON':{'vlocity_cmt__ServiceAccountId__c':'0017a00002PTQfaAAH','vlocity_cmt__BillingAccountId__c':'0017a00002HIrh4AAD'}
        }

        res2=DR_IP.remoteClass('CPQUtils','putCartsItems',inp2,{})

        inp2 = {
            'orderId':orderId,
      #      'cartItems':cartItems,
            'value':productCode,
            'cartNodes':res['cartNodes'],
      #      'returnPayload':True,
            'updateAttributeJSON':{'ATT_DELIVERY_METHOD':'Técnico'},
            'updateFieldsJSON':{'vlocity_cmt__ServiceAccountId__c':'0017a00002HIrh4AAD','vlocity_cmt__BillingAccountId__c':'0017a00002PTQfaAAH'}

        }

        res3=DR_IP.remoteClass('CPQUtils','putCartsItems',inp2,{})

        print()

    def postCartsPromoItems(self,orderId,cartNodes,promoId):
        inp2 = {
            'orderId':orderId,
         #   'cartItems':cartItems,
         #   '95':productCode,
            'cartNodes':cartNodes,
            'promotionId':promoId
        }

        res2=DR_IP.remoteClass('CPQUtils','postCartsPromoItems',inp2,{})

        return res2
    
    def test_getHierarchy_and_postPromoItems(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xL5MAAU'
        productCode = 'C_E-SIM_CARD'
        promotionId_trial = 'a507a0000005BjjAAE'
        promotionId_Movel = 'a507a0000005BiDAAU'

        cartItems = CPQAppHandler.getCartsItems(orderId)
        filename = jsonFile.write('cartItems',cartItems)

        inp = {
            'cartItems':cartItems,
            'value':productCode,
            'itemType':'lineItem'
        }
        res=DR_IP.remoteClass('CPQUtils','getcartNodes',inp,{})

        inp2 = {
            'orderId':orderId,
            'cartItems':cartItems,
            'value':productCode,
            'cartNodes':res['cartNodes'],
            'promotionId':promotionId_trial
            ,'returnPayload':True
        }

        res2=DR_IP.remoteClass('CPQUtils','postCartsPromoItems',inp2,{})

        if 'returnPayload' in inp2 and inp2['returnPayload'] == True:
            filename = jsonFile.write('funcionndo_test1234',res2['data'])


        inp2['promotionId'] = promotionId_Movel
        res2=DR_IP.remoteClass('CPQUtils','postCartsPromoItems',inp2,{})


        print()

    def test_postCartItem(self):
        restClient.init('NOSQSM')

        orderId = '8017a000002xGaJAAU'
        productCode = 'C_SIM_CARD'
        cartItems = CPQAppHandler.getCartsItems(orderId)

        inp = {
            'orderId':orderId,
            'cartItems':cartItems,
            'key':'ProductCode',
            'value':productCode
        }
        res=DR_IP.remoteClass('CPQUtils','postCartItem',inp,{})

        filename = jsonFile.write('no_funcionndo_test1234',res['data'])

        res['data']['items'][0]['parentRecord']['records'][0]['lineItems']['records'] = []
        res['data']['items'][0]['parentRecord']['records'][0]['productCategories']['records'] = []

        res2 = CPQAppHandler.call('postCartItem',res['data'])

        print()


    def test_postCartItem_handler(self):
        restClient.init('NOSQSM')

        orderId = '8017a000002xGaJAAU'
        productCode = 'C_SIM_CARD'
        cartItems = CPQAppHandler.getCartsItems(orderId)

        inp = {
            'orderId':orderId,
            'cartItems':cartItems,
            'key':'ProductCode',
            'value':productCode
        }
        res=DR_IP.remoteClass('CPQUtils','postCartItem',inp,{})

        filename = jsonFile.write('no_funcionndo_test1234',res['data'])


        res['data']['items'][0]['parentRecord']['records'][0]['lineItems']['records'] = []
        res['data']['items'][0]['parentRecord']['records'][0]['productCategories']['records'] = []

        res2 = CPQAppHandler.call('postCartItem',res['data'])


        print()

    def test_brute(self):
        restClient.init('NOSQSM')

        input = {
            "methodName": "xxxxxx",
            "price": False,
            "validate": False,
            "includeAttachment": False,
            "hierarchy": 5,
            "orderId":"8017a000002xGaJAAU"
            }
        
        res2 = CPQAppHandler.call('putCartsItems',input)

        a=1


    def test_query(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xIzaAAE'
        q = f"select  vlocity_cmt__AssetReferenceId__c from OrderItem where OrderId ='{orderId}' order by vlocity_cmt__ServiceAccountId__r.NOS_t_IdConta__c desc limit 1"

        inp2 = {
            'query':q
        }
        res2=DR_IP.remoteClass('CPQUtils','query',inp2,{})

        a=1


    def print_attributes(self,cartNodes):
        print('------------------------------------------')
        for attcat in cartNodes[0]['attributeCategories']['records']:
            print(f"{attcat['Name']}  {attcat['Code__c']}")
            for prodcat in attcat['productAttributes']['records']:
                print(f"       {prodcat['code']}   {prodcat['label']} ")
                a=1

    def test_execute(self):
        restClient.init('NOSQSM')


       # amendOrderId = AMEND %orderId%
       # CHECKOUT %amendOrderId%

        instruction = '''
        getCartsItems %amendOrderId%
        postCartItems %TV_equip_code%
        getCartsItems %amendOrderId%
        postCartsPromoItems %TV_equip_code%
        accountId = QUERY "select vlocity_cmt__AssetReferenceId__c, Product2.Name, vlocity_cmt__Action__c from OrderItem where OrderId = %amendOrderId% order by vlocity_cmt__ServiceAccountId__r.NOS_t_IdConta__c desc"
        putCartsItems %amendOrderId% %TV_equip_code% ATT_NOS_DELIVERY_METHOD="Técnico", vlocity_cmt__ServiceAccountId__c=accountId, vlocity_cmt__BillingAccountId__c=accountId
        equipmentId = QUERY "select  vlocity_cmt__AssetReferenceId__c, Product2.Name, vlocity_cmt__Action__c from OrderItem where OrderId = %amendOrderId% order by vlocity_cmt__ServiceAccountId__r.NOS_t_IdConta__c desc"
        putCartsItems %amendOrderId% %150Channelds% ATT_EQUIP_ID:%equipmentId%
        '''

        input = {
            'intructions':instruction,
            'data':{
                '150Channelds':'C_NOS_SERVICE_TV_003',
                'TV_equip_code':'C_NOS_EQUIP_TV_017',
                'amendOrderId':'8017a000002xIzaAAE'
            }
        } 

        res2=DR_IP.remoteClass('CPQUtilsExecute','preProcess',input,{})

        a=1


    def test_a(self):

        input = {
            'orderId':'',
            'TV_equip_code':'',
            '150Channelds':''
        }
        instruction = '''
        amendOrderId = AMEND %orderId%
        POST_CARTS_ITEMS TV_equip_code
        accountId = QUERY "select  vlocity_cmt__AssetReferenceId__c, Product2.Name, vlocity_cmt__Action__c from OrderItem where OrderId = $orderId order by vlocity_cmt__ServiceAccountId__r.NOS_t_IdConta__c desc"
        PUT_CART_ITEMS ATT_NOS_DELIVERY_METHOD="Técnico", vlocity_cmt__ServiceAccountId__c=accountId, vlocity_cmt__BillingAccountId__c=accountId
        equipmentId = QUERY "select  vlocity_cmt__AssetReferenceId__c, Product2.Name, vlocity_cmt__Action__c from OrderItem where OrderId = $orderId order by vlocity_cmt__ServiceAccountId__r.NOS_t_IdConta__c desc"
        PUT_CART_ITEMS 150Channelds {'ATT_EQUIP_ID':equipmentId}
        '''


    def test_nos4(self):
        restClient.init('NOSQSM')
        orderId = '8017a000002xIzaAAE'
        
        productCode = 'C_NOS_EQUIP_TV_017'
        channels_150 = 'C_NOS_SERVICE_TV_003'

        cartItems = CPQAppHandler.getCartsItems(orderId)


        if 1==2:
            ph = self.getcartNodes(cartItems,productCode)
            ci = self.postCartItems(orderId,ph['cartNodes'])
            cartItems = CPQAppHandler.getCartsItems(orderId)

        ph = self.getcartNodes(cartItems,productCode,itemType='lineItem')



        if 1==2:
            root = ph['cartNodes'][-1]

            for promo in root['promotions']['records']:
                print(promo['Id'])
                pr = self.postCartsPromoItems(orderId,ph['cartNodes'],promo['Id'])


        self.print_attributes(ph['cartNodes'])

        res4 = self.putCartItems(orderId,ph['cartNodes'],{'ATT_NOS_DELIVERY_METHOD':'Técnico'},{'vlocity_cmt__ServiceAccountId__c':'0017a00002HIrh4AAD','vlocity_cmt__BillingAccountId__c':'0017a00002PTQfaAAH'})


        q = f"select  vlocity_cmt__AssetReferenceId__c, Product2.Name, vlocity_cmt__Action__c from OrderItem where OrderId ='{orderId}' order by vlocity_cmt__ServiceAccountId__r.NOS_t_IdConta__c desc"
        inp2 = {
            'query':q
        }
        res2=DR_IP.remoteClass('CPQUtils','query',inp2,{})

        ph = self.getcartNodes(cartItems,channels_150,itemType='lineItem')
        self.print_attributes(ph['cartNodes'])

        res4 = self.putCartItems(orderId,ph['cartNodes'],{'ATT_EQUIP_ID':res2['response'][0]['vlocity_cmt__AssetReferenceId__c']})

        a=1
        
    def test_queue_get(self):
        restClient.init('NOSQSM')

        instruction = '''
        getCartsItems %amendOrderId%
        putCartsItems %productCode% ATT_NOS_DELIVERY_METHOD='Técnico', vlocity_cmt__ServiceAccountId__c=0017a00002PTQfaAAH, vlocity_cmt__BillingAccountId__c=0017a00002PTQfaAAH
        '''

        input = {
            'intructions':instruction,
            'data':{
                'amendOrderId':'8017a000002xIzaAAE',
                'orderId':'8017a000002xIzaAAE',
                'productCode':'C_NOS_EQUIP_TV_017'
            }
        } 

        res2=DR_IP.remoteClass('CPQUtilsExecute','execute',input,{})

        input = {
            'orderId':'8017a000002xIzaAAE'
        }

        res2=DR_IP.remoteClass('CPQUtils','getCartsItems',input,None)


        a=1
#'serverResponse: [{"errorCode":"APEX_ERROR","message":"System.JSONException: Apex Type unsupported in JSON: Schema.SObjectType\\n\\n(System Code)"}]'

    def test_getCartItems2(self):       
        restClient.init('NOSQSM')
        input = {
            'orderId':'8017a000002xIzaAAE'
        }
        res1=DR_IP.remoteClass('CPQUtils','getCartsItems',input,None)


        res2 = CPQAppHandler.getCartsItems('8017a000002xIzaAAE')
        filename = jsonFile.write('funcionndo_test1234',res2)


        res3=DR_IP.remoteClass('CPQUtils','getCartsItemsSimple',input,None)
        filename = jsonFile.write('no_funcionndo_test1234',res3['response'])

        a=1

    def test_getCartItems2p(self):       
        restClient.init('NOSQSM')
        orderId = '8017a000002xM5JAAU'
        productCode = 'C_NOS_EQUIP_TV_017'
        new = False

        if new == False:
           # cartItems = CPQAppHandler.getCartsItems(orderId)

            input = {
                'orderId':orderId,
                'key':'ProductCode',
                'value':productCode
            }
            if 1==2:
                res3=DR_IP.remoteClass('CPQUtils','getCartsItemsSimple',input,None)
                cartItems = res3['response']
                inp = {
                    'cartItems':cartItems,
                    'key':'ProductCode',
                    'value':productCode
                }
                res3=DR_IP.remoteClass('CPQUtils','getcartNodes',input,{})    
            else:  
                res3=DR_IP.remoteClass('CPQUtils','getCartsNodes',input,{})        
            filename = jsonFile.write('funcionndo_test1234',res3)

        else:
            input = {
                'orderId':orderId,
                'key':'ProductCode',
                'value':productCode
            }
            res3=DR_IP.remoteClass('CPQUtils','getCartsItemsSimple',input,None)
            filename = jsonFile.write('no_funcionndo_test1234',res3)

        inp2 = {
            'orderId':orderId,
          #  'cartItems':cartItems,
          #  'value':productCode,
            'cartNodes':res3['cartNodes']
        }

        res=DR_IP.remoteClass('CPQUtils','postCartItems',inp2,{})
        a=1
    def test_put_new(self):       
        restClient.init('NOSQSM')
        orderId = '8017a000002xM5JAAU'
        productCode = 'C_NOS_EQUIP_TV_017'

        input = {
            'orderId':orderId,
            'key':'ProductCode',
            'value':productCode,
            'itemType':'lineItem'
        }
        
        res=DR_IP.remoteClass('CPQUtils','getCartsNodes',input,{})       
        filename = jsonFile.write('xxx',res)

        input = {
            'orderId':orderId,
            'cartNodes':res['cartNodes'],
            'updateAttributeJSON':{'ATT_NOS_DELIVERY_METHOD':'Técnico'},
            'updateFieldsJSON':{'vlocity_cmt__ServiceAccountId__c':'0017a00002HIrh4AAD','vlocity_cmt__BillingAccountId__c':'0017a00002PTQfaAAH'}
        }  


        if 1==2:
            res2=DR_IP.remoteClass('CPQUtils','putCartsItems',input,{})
        else:
            for promo in res['cartNodes'][4]['promotions']['records']:
                input = {
                        'orderId':orderId,
                        'cartNodes':res['cartNodes'],
                        'promotionId':promo['Id']
                    }
                res2=DR_IP.remoteClass('CPQUtils','postCartsPromoItems',input,{})

        return res2

    def test_post_new(self):       
        restClient.init('NOSQSM')
        orderId = '8017a000002xOA2AAM'
        productCode = 'C_NOS_EQUIP_TV_018'

        input = {
            'orderId':orderId,
            'key':'ProductCode',
            'value':productCode,
          #  'itemType':'lineItem'
        }
        
        res=DR_IP.remoteClass('CPQUtils','getCartsNodes',input,{})       
        filename = jsonFile.write('xxx',res)

        inp2 = {
            'orderId':orderId,
          #  'cartItems':cartItems,
          #  'value':productCode,
            'cartNodes':res['cartNodes']
            ,'returnPayload':True

        }

        res=DR_IP.remoteClass('CPQUtils','postCartItems',inp2,{})
        filename = jsonFile.write('xxx1',res)

        a=1