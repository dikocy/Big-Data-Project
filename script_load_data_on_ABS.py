import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Connection au compte de stockage...")
    # permet d'obtenir la clé d'acces de notre compte de stocage enrégistré dans nos variable d'environnement
    connect_str = os.getenv('CONNECT_STR')

    # Creation d'un objet blob_service_client qui nous permettra de creer un container
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Creation du container à partir de l'objet blob instancier ci-dessus
    #print("Creation du container...")
    container_name = "transactionsdata"
    #container_client = blob_service_client.create_container(container_name)

    blob_client = blob_service_client.get_blob_client(container=container_name, blob='transactions.csv')
    # charger le fichier crée
    with open("transactions.csv", "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)
