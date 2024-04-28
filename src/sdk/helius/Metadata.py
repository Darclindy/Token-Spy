from sdk.helius.Context import NFTAPI
from utils.out import write_to_file
import json

'''
[{'mint': 'ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82', 'onChainData': {'tokenStandard': 'Fungible', 'key': 'MetadataV1', 'updateAuthority': 'E4X8Fihh8RHwwtCPN4XFUFc1F7iygBX3evfLjQnMFak9', 'mint': 'ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82', 'data': {'name': 'BOOK OF MEME', 'symbol': 'BOME', 'uri': 'https://bafkreifxe2oxpn45fkmpy7sitkzgipmznewphi23rk5n4hzwve7jp57tmu.ipfs.nftstorage.link', 'sellerFeeBasisPoints': 0, 'creators': None}, 'primarySaleHappened': False, 'isMutable': True, 'editionNonce': 254, 'uses': {'useMethod': '', 'remaining': 0, 'total': 0}, 'collection': None, 'collectionDetails': None}, 'offChainData': {'description': 'https://2shoc6fvrmkaeovsta7mkmicjzy2sellt5l45nxsrsz6ti436jfq.arweave.net/1I7heLWLFAI6spg-xTECTnGpEWufV8628oyz6aOb8ks', 'image': 'https://bafkreihztk5poge7f2lz6logfjmhc7h7u6shvgacoktnuezks5oblmieue.ipfs.nftstorage.link', 'name': 'BOOK OF MEME', 'symbol': 'BOME'}}]
'''

def get_token_symbol(mint_address):
    mint_accounts = [mint_address]
    nft_metadata = NFTAPI.get_nft_metadata(mint_accounts=mint_accounts)
    # write_to_file("metadata.json", json.dumps(nft_metadata))
    try:
        return nft_metadata[0]["onChainData"]["data"]["symbol"]
    except: 
        print(nft_metadata)
        write_to_file("logs.json", json.dumps(nft_metadata))
        return "ERROR"

def get_token_name(mint_address):
    mint_accounts = [mint_address]
    nft_metadata = NFTAPI.get_nft_metadata(mint_accounts=mint_accounts)
    # write_to_file("metadata.json", json.dumps(nft_metadata))
    try:
        return nft_metadata["onChainData"]["data"]["name"]
    except:
        return "ERROR"

def get_token_symbols(address_list) -> list:
    nft_metadata = NFTAPI.get_nft_metadata(mint_accounts=address_list)
    write_to_file("metadata.json", json.dumps(nft_metadata))
    symbols = []
    for item in nft_metadata:
        try:
            symbols.append(item["onChainData"]["data"]["symbol"])
        except:
            symbols.append("Error")
    return symbols

if __name__ == "__main__":
    get_token_symbol("")