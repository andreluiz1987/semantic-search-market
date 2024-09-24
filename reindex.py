from elasticsearch_connection import ElasticsearchConnection

client = ElasticsearchConnection().get_client()


def reindex(source, dest):
    response = client.reindex(source={
        "index": source
    }, dest={
        "index": dest
    }, wait_for_completion=False)
    print(response)


if __name__ == '__main__':
    reindex("grocery-catalog", "grocery-catalog-elser")
