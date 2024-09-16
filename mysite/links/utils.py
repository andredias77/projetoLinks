# from paapi5_python_sdk.api.default_api import DefaultApi
# from paapi5_python_sdk import GetItemsRequest, PartnerType
# from paapi5_python_sdk.rest import ApiException
# # Configurar suas credenciais da Amazon Product Advertising API
# access_key = 'AKIAIAP63C5KYDUU6BTA'
# secret_key = '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'
# partner_tag = 'andredias60c-20'
# marketplace = "webservices.amazon.com.br"  # Use o marketplace correto, como .com ou .br

# # Instanciar a API
# api_instance = DefaultApi(access_key, secret_key, partner_tag, marketplace)

# def obter_detalhes_produto_amazon(asin):
#     try:
#         # Definir a solicitação da API com o ASIN (Amazon Standard Identification Number)
#         get_items_request = GetItemsRequest(
#             item_ids=[asin],  # ASIN do produto
#             partner_tag=partner_tag,
#             partner_type=PartnerType.ASSOCIATES

#         )

#         # Fazer a requisição à API
#         api_response = api_instance.get_items(get_items_request)

#         # Extrair detalhes do produto da resposta da API
#         if api_response.items_result.items:
#             item = api_response.items_result.items[0]  # Primeiro item retornado
#             nome_produto = item.item_info.title.display_value
#             imagem_url = item.images.primary.large.url  # URL da imagem do produto

#             return {
#                 'nome_produto': nome_produto,
#                 'imagem_url': imagem_url
#             }
#         else:
#             print("Produto não encontrado pela API.")
#             return None

#     except ApiException as e:
#         print(f"Erro ao buscar detalhes do produto na API da Amazon: {e}")
#         return None

