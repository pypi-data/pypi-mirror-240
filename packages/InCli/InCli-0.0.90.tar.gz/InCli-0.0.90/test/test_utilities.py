import unittest,simplejson
from InCli.SFAPI import restClient,query,Sobjects,tooling

class Test_Utilities(unittest.TestCase):
    def test_limits(self):
        restClient.init('DEVNOSCAT2')
        action = '/services/data/v51.0/limits'
        res = restClient.callAPI(action)

        print()

    def test_id(self):
        restClient.init('DEVNOSCAT2')
        action = '/services/data/v51.0'
        res = restClient.callAPI(action)

        print()

    def test_id(self):
        restClient.init('DEVNOSCAT2')
        action = '/services/data/v51.0'
        res = restClient.callAPI(action)
        for key in res.keys():
            print()
            action = res[key]
            res1 = restClient.callAPI(action)
            print(action)
            print(res1)

        print()
    
    def test_select(self):
        restClient.init('DEVNOSCAT4')

        q = f"select fields(all) from vlocity_cmt__VlocityTrackingEntry__c order by vlocity_cmt__Timestamp__c desc limit 100"
        res = query.query(q)
        for r in res['records']:
            ll = simplejson.loads(r['vlocity_cmt__Data__c'])
            json_formatted_str = simplejson.dumps(ll, indent=2, ensure_ascii=False)
            print(json_formatted_str)
            print()
            
    def test_delete_logs(self):
        restClient.init('NOSPRD')

        userId = Sobjects.IdF('User','username:u1003015@nos.pt')

        q = f"select Id from ApexLog where LogUserId='{userId}' "
        res = query.query(q)

        id_list = [record['Id'] for record in res['records']]

        
        Sobjects.deleteMultiple('ApexLog',id_list)
        print()

    def delete(self,q):
        res = query.query(q)

        id_list = [record['Id'] for record in res['records']]
        
        print(f"deleteing {len(id_list)} rows.")

        Sobjects.deleteMultiple('ApexLog',id_list)
        print()

    def test_delete_allRows(self):
        restClient.init('DEVNOSCAT3')

        q = "select Id from vlocity_cmt__Element__c "

        self.delete(q)

    def test_deleteAllRows_multiple(self):
        restClient.init('DEVNOSCAT3')
        self.delete("select Id from vlocity_cmt__OmniScript__c ")
        self.delete("select Id from vlocity_cmt__Element__c ")

        self.delete("select Id from vlocity_cmt__DRMapItem__c ")
        self.delete("select Id from vlocity_cmt__ObjectSection__c ")
        self.delete("select Id from vlocity_cmt__AttributeAssignment__c ")
        self.delete("select Id from vlocity_cmt__CalculationMatrixRow__c ")
        self.delete("select Id from vlocity_cmt__AsyncProcessJob__c ")
        self.delete("select Id from vlocity_cmt__OrchestrationItem__c ")
        self.delete("select Id from vlocity_cmt__ObjectFacet__c ")
        self.delete("select Id from vlocity_cmt__PriceListEntry__c ")
        self.delete("select Id from vlocity_cmt__Attribute__c ")
        self.delete("select Id from vlocity_cmt__ProductChildItem__c ")
        self.delete("select Id from order ")


    def test_delete_anonumous(self):
        restClient.init('DEVNOSCAT2')

        object_name = 'vlocity_cmt__CachedAPIResponse__c'
        code = f"delete[SELECT id FROM {object_name} LIMIT 10000];"

        res = tooling.executeAnonymous(code)
        a=1


    def test_delete_something(self):
        restClient.init('DEVNOSCAT2')
        self.delete("select Id from vlocity_cmt__CachedAPIResponse__c ")

        s=1

    def test_getAssret(self):
        q = f"select fields(all) from asset where vlocity_cmt__RootItemId__c='{assetId}' limit 200"

    def test_querySomething(self):
        restClient.init('NOSDEV')
        q = f"select fields(all) from EventLogFile limit 200"

        call = query.query(q)

        print()

    def test_delete_fulfil(self):
        restClient.init('DEVNOSCAT4')

        q = "select Id from vlocity_cmt__FulfilmentRequestDecompRelationship__c  "
        self.delete(q)

        q = "select Id from vlocity_cmt__FulfilmentRequestLineDecompRelationship__c  "
        self.delete(q)
        
        q = "select Id from vlocity_cmt__FulfilmentRequest__c  "
        self.delete(q)

        q = "select Id from vlocity_cmt__InventoryItem__c  "
        self.delete(q)

        q = "select Id from vlocity_cmt__InventoryItemDecompositionRelationship__c  "
        self.delete(q)

        q = "select Id from AssetRelationship  "
        self.delete(q)

        q = "select Id from vlocity_cmt__OrderAppliedPromotionItem__c  "
        self.delete(q)

    def test_call_something(self):
        restClient.init('NOSQSM')

       # res = restClient.requestWithConnection(action='resource/1641908190000/vlocity_cmt__OmniscriptLwcCompiler')
        res = restClient.requestRaw('https://nos--nosqms.sandbox.my.salesforce.com/resource/1641908190000/vlocity_cmt__OmniscriptLwcCompiler')

        print(res)
        print()

    def test_iJoin_code(self):
        restClient.init('NOSQSM')

        name = 'd9b0fe97-8d5a-b2b6-8293-f5abe8f4b675'

        q = f"select name, Content__c from Dataframe__c where name ='{name}' "

        res = query.query(q)

        print(res['records'][0]['Content__c'])
       # print(res)
        print()

    def test_update_something(self):
        restClient.init('NOSQSM')

        Sobjects.update()

    def test_inventory_stuff(self):
        restClient.init('NOSDEV')

        accountId ='0013O00001B0lHvQAJ'

        q = f"select fields(all) from asset where accountid='{accountId}' limit 100"

        call = query.query(q)

        assetIds = [asset['Id'] for asset in call['records']]

        q = f"select fields(all) from vlocity_cmt__InventoryItemDecompositionRelationship__c where vlocity_cmt__SourceAssetId__c in ({query.IN_clause(assetIds)}) limit 100"

        call2 = query.query(q)

        sourceInventoryItemIds = [rel['vlocity_cmt__SourceInventoryItemId__c'] for rel in call2['records'] if rel['vlocity_cmt__SourceInventoryItemId__c']!=None]
        destinationInventoryItemIds = [rel['vlocity_cmt__DestinationInventoryItemId__c'] for rel in call2['records'] if rel['vlocity_cmt__DestinationInventoryItemId__c'] != None]

        q = f"select fields(all) from vlocity_cmt__InventoryItem__c where Id in ({query.IN_clause(destinationInventoryItemIds)}) limit 100"

        call3 = query.query(q)

        q= f"select fields(all) from vlocity_cmt__InventoryItem__c  where vlocity_cmt__AccountId__c='{accountId}' limit 100"

        call4 = query.query(q)

        a=1

    def test_storage(self):
        restClient.init('NOSPRD')

        q_total = "SELECT vlocity_cmt__IsActive__c,Name, vlocity_cmt__Type__c, vlocity_cmt__SubType__c, vlocity_cmt__Language__c,  Id,vlocity_cmt__OmniProcessType__c  from vlocity_cmt__OmniScript__c   where vlocity_cmt__OmniProcessType__c = 'OmniScript'"
        res = query.query(q_total)

        q_elements_total = "select count(Id) from vlocity_cmt__Element__c"
        res = query.query(q_elements_total)

        q_unique = "SELECT vlocity_cmt__IsActive__c,Name, vlocity_cmt__Type__c, vlocity_cmt__SubType__c, vlocity_cmt__Language__c,  Id,vlocity_cmt__OmniProcessType__c  from vlocity_cmt__OmniScript__c   where vlocity_cmt__IsActive__c = true and vlocity_cmt__OmniProcessType__c = 'OmniScript'"

        res = query.query(q_unique)

        total_elements = 0

        for omni in res['records']:
            q2 = f" select count(Id) from vlocity_cmt__Element__c where vlocity_cmt__OmniScriptId__c ='{omni['Id']}'"
            res2 = query.query(q2)
            elements = res2['records'][0]['expr0']
            total_elements = total_elements + elements
            print(f"{omni['Name']}  {elements}")
            a=1

        a=1

    def test_storage_orchestration(self):
        restClient.init('NOSPRD')

        plan_id = 'a457T0000015OchQAE'

        q_items = f"select Id,Name from vlocity_cmt__OrchestrationItem__c where vlocity_cmt__OrchestrationPlanId__c = '{plan_id}'"

        r1 = query.query(q_items)

        itemIds = [rec['Id'] for rec in r1['records']]

        q_source = f"select Id,vlocity_cmt__OrchestrationItemId__c,vlocity_cmt__SourceOrderItemId__c from vlocity_cmt__OrchestrationItemSource__c where vlocity_cmt__OrchestrationItemId__c in ({query.IN_clause(itemIds)})"

        r2 = query.query(q_source)

        q_dependency = f"select Id,Name,vlocity_cmt__OrchestrationItemId__c from vlocity_cmt__OrchestrationDependency__c where vlocity_cmt__OrchestrationItemId__c in ({query.IN_clause(itemIds)})"

        r3 = query.query(q_dependency)

        a=1