from dune_client.types import QueryParameter
from dune_client.query import QueryBase
import sdk.dune.Context as Context



class BaseQuery:
    __name__ = "Sample Query"
    __query_id__= 0
    __params__ = []

    def run_query(self):
        query = QueryBase(
            name= self.__name__,
            query_id=self.__query_id__,
            params=self.__params__
        )

        return Context.dune_client.run_query(query=query, performance='medium')

    
    def __init__(self, name="", query_id=0, params=[]) -> None:
        __name__ = name
        self.__query_id__ = query_id
        self.__params__.append(params)


class DemoQuery(BaseQuery):
    __name__ = "Demo Query"
    __query_id__ = 3535049
    __params__ = [
        QueryParameter.text_type(name="mint_address", value="4G86CMxGsMdLETrYnavMFKPhQzKTvDBYGMRAdVtr72nu"),
    ]


if (__name__ == "__main__"):
    demo = DemoQuery(params=[
        QueryParameter.text_type(name="mint_address", value="4G86CMxGsMdLETrYnavMFKPhQzKTvDBYGMRAdVtr72nu")
    ])

    result = demo.run_query()

    print(result)

    





