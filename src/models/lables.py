from ctypes import Union
import json
import openai
import requests
import openai
from tinydb import TinyDB
from prompt import get_response
from google.generativeai.types import GenerateContentResponse

from torob_category import CategoryDto, CategoryProductDTO
from torob_product import ProductDTO, VarientItem

openai.api_key = "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"  # Replace with your actual token
openai.api_base = "http://127.0.0.1:1337/v1"

class AppUrls:
    base_url = "https://api.torob.com/v4"

    @staticmethod
    def category_url(category_id = "94", page:str = "0", size:str="100"):
        return f"{AppUrls.base_url}/base-product/search/?category=94&category_id=94&available=true&sort=popularity&page={page}&size={1000}&source=next_desktop"
    
    @staticmethod
    def generate_prodcut_url(product_id):
        return f"{AppUrls.base_url}/base-product/details-log-click/?source=next_desktop&discover_method=browse&_bt__experiment=&prk={product_id}"


class TorobBot:
    def __init__(self) -> None:
        self.client = requests.Session()
        self.db = TinyDB('db.json')

    def _generate_product_desc(self, title:str):
        '''
        # Product Descrition generation.

        by using the chatgpt api generated descrition for products with this query `"یک مقاله برای معرفی {title} به زبان فارسی.بنویس"`
        after getting resposne by `Map` type we should getting this item from this path `response['choices'][0]['message']['content']`
        now can access to generated description of product with ChatGpt.
        '''
        context = {
            "role":"system",
            "content": f'''
# Context:
you have product with this name: {title}. write a article for this product to persian language.

# Answer Rules:
- persian language.
- contain list 5 benefit of product.
- contain list Weaknesses of product.
- use html format to generate desc and use heading tags.
- optimaze article SEO for search engain.
'''
        }

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[context,{"role": "user", "content": f"یک مقاله برای معرفی {title} .بنویس"}],
        stream=False,
    )
        return response["choices"][0]["message"]['content']

    def get_category_products_object(self, category:CategoryDto = CategoryDto(name="", id="175"), page:str = "1") -> None | list[CategoryProductDTO]:
        '''
        # Getting Products list form Torob.ir

        request to torob api and getting the list of product there is a category. if category item in pageUrl method is empty
        by default request for `175` category id.
        '''
        print("cat id",category.id,AppUrls.category_url(category_id=category.id))
        response = self.client.get(AppUrls.category_url(category_id=category.id)).json()['results']
        data = []
        if (response):
            for item in response:
                c = CategoryProductDTO(**item)
                c.category_id = category.id
                data.append(c)
            return data
        return None

    def get_product(self,item: CategoryProductDTO) -> ProductDTO:
        """get product information from CategoryProductDto object

        Args:
            item (CategoryProductDTO): product from category

        Returns:
            ProductDTO: product full information
        """    
            
        response = self.client.get(item.more_info_url).json()
        min_offer, metadata = self._get_product_metadata(response)
        try:
            attributes = self._get_product_attributes(response=response)
        except:
            attributes = []
        
        return ProductDTO(**{
            "id": response['random_key'],
            "name": response['name1'],
            "type": "simple",
            "status": "draft",
            "min_price": response['min_price'],
            "max_price": response['max_price'],
            "buy_box_price_text": response['buy_box_price_text'],
            "variants": response['variants'],
            "category" : item.category_id,
            "regular_price": min_offer['price'],
            "description": None,
            "short_description": response['name1'],
            "images": [
                {"src":response['image_url']}
            ],
            "meta_data": metadata,
            "attributes" : attributes
        }) 

    def _find_min_offer(self,information):
        '''
        # Finding chipper than price

        check the all product seller and select the best price seller product.
        :args => information : json
        :return => json : Dict
        '''
        offers = information['products_info']['result']
        min = offers[0]
        for index in range(len(offers)):
            if (offers[index]['price_text_mode'] == "active") and (int(min['price']) > int(offers[index]['price'])) :
                min = offers[index]

        return min

    def _get_product_attributes(self,response):
        '''Extract product all information.

        Args:
            response (any) : Torob api response
        Return:
            attributes (Dict[str,str]) : prodcut attributes item
        '''
        informations = response['structural_specs']['headers'][0]['specs']
        attributes = []
        temp = list(informations.items())
        for value in temp:
            
            data = {
                "name": value[0],
                "slug": value[0].replace(" ","_"),
                "options": [value[1]],
                "visible": True
            }
            attributes.append(data)
        return attributes

    def _get_product_metadata(self, response:any):
        """extract product metadata and generate ro serializer format.

        Args:
            response (any): a json of response form categoryProduct more_info_url property

        Returns:
            min_offer (Dict[str,str]): product best offer for sell product
            metadata (List[Dict[str,str]]): product metadata json
        """        
        metadata = []
        min_offer = self._find_min_offer(response)
        temp = list(min_offer.items())
        for value in temp:
            data = {
                "key": value[0],
                "value": value[1]
            }
            metadata.append(data)
        return  min_offer, metadata
    
    def get_product_varient_information(self, varient:VarientItem):
        product = self.get_product(CategoryProductDTO(more_info_url=varient.more_info_url))
        return product



if __name__ == "__main__":
    item = TorobBot()
    products = item.get_category_products_object(category=CategoryDto(name="",id="94"))
    items = []
    counter = 1

    for p in products:
        # product = item.get_product(p)
        res = get_response(p.name2)
        if (res is not None):
            items.append({
                "post": p.__dict__,
                "content": res
            })
            open("data.json", "w").write(json.dumps(items, ensure_ascii=False))
            print("Add index:",counter, end="\r")
            counter+=1

    print("Add index:",counter, end="\r")

