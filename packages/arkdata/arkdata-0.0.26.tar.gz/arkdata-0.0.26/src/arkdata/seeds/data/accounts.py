from arkdata import models


def seed():
    items = [
        {
            "xuid": "123",
            "player_id": "123",
            "player_name": "zed3kiah",
            "tribe_id": "123",
            "tribe_name": "Pineapple",
            "berry_bush_seeds": 10659,
            "influence_points": 10912,
            "nitrado_id": "QFIhYrgDvnH",
            "server_id": "123"
        },
        {
            "xuid": "02670680",
            "player_id": "221067",
            "player_name": "rlettuce0",
            "tribe_id": "102477",
            "tribe_name": "Mynte",
            "berry_bush_seeds": 10659,
            "influence_points": 10912,
            "nitrado_id": "QFIhYrgDvnH",
            "server_id": "2673763"
        },
        {
            "xuid": "32469606",
            "player_id": "655047",
            "player_name": "aherculson1",
            "tribe_id": "009604",
            "tribe_name": "Meetz",
            "berry_bush_seeds": 10447,
            "influence_points": 10257,
            "nitrado_id": "99kymFhNtqz",
            "server_id": "7656407"},
        {
            "xuid": "37694979",
            "player_id": "077877",
            "player_name": "cclace2",
            "tribe_id": "708739",
            "tribe_name": "Flashset",
            "berry_bush_seeds": 10187,
            "influence_points": 10341,
            "nitrado_id": "6DhJ2Y6zS7u",
            "server_id": "9039778"
        },
        {
            "xuid": "05203671",
            "player_id": "163616",
            "player_name": "wwoodlands3",
            "tribe_id": "347919",
            "tribe_name": "Browsecat",
            "berry_bush_seeds": 1094,
            "influence_points": 10361,
            "nitrado_id": "NzZsTvopbpr",
            "server_id": "3826176"
        },
        {
            "xuid": "14131099",
            "player_id": "670019",
            "player_name": "lshimmin4",
            "tribe_id": "510493",
            "tribe_name": "Jazzy",
            "berry_bush_seeds": 10380,
            "influence_points": 10423,
            "nitrado_id": "GurwujYKG4t",
            "server_id": "5033548"
        },
        {
            "xuid": "46610162",
            "player_id": "935910",
            "player_name": "jmccarrison5",
            "tribe_id": "884381",
            "tribe_name": "Thoughtmix",
            "berry_bush_seeds": 10359,
            "influence_points": 10319,
            "nitrado_id": "h927kX86uTL",
            "server_id": "3237766"
        },
        {
            "xuid": "82588774",
            "player_id": "345261",
            "player_name": "chandlin6",
            "tribe_id": "527133",
            "tribe_name": "Plambee",
            "berry_bush_seeds": 10864,
            "influence_points": 10535,
            "nitrado_id": "Z7CUz2thXHY",
            "server_id": "7615679"
        },
        {
            "xuid": "83510641",
            "player_id": "372375",
            "player_name": "kschoenfisch7",
            "tribe_id": "425808",
            "tribe_name": "Riffwire",
            "berry_bush_seeds": 10705,
            "influence_points": 10008,
            "nitrado_id": "WLV6fwpxgOH",
            "server_id": "5404459"
        },
        {
            "xuid": "92939552",
            "player_id": "854343",
            "player_name": "ssiggens8",
            "tribe_id": "844781",
            "tribe_name": "Kaymbo",
            "berry_bush_seeds": 10954,
            "influence_points": 10510,
            "nitrado_id": "lDoNdU0MbLv",
            "server_id": "3419515"
        },
        {
            "xuid": "76506392",
            "player_id": "463520",
            "player_name": "mkelmere9",
            "tribe_id": "646710",
            "tribe_name": "Twitterwire",
            "berry_bush_seeds": 10845,
            "influence_points": 10921,
            "nitrado_id": "8b15ctFYl1g",
            "server_id": "8221537"
        },
        {
            "xuid": "09897611",
            "player_id": "360584",
            "player_name": "tsillea",
            "tribe_id": "977799",
            "tribe_name": "Yata",
            "berry_bush_seeds": 10377,
            "influence_points": 10424,
            "nitrado_id": "a2UjqLyF2a5",
            "server_id": "4537924"
        },
        {
            "xuid": "80058538",
            "player_id": "818938",
            "player_name": "cmcnicolb",
            "tribe_id": "909322",
            "tribe_name": "Jabbersphere",
            "berry_bush_seeds": 10187,
            "influence_points": 10911,
            "nitrado_id": "ZA54mXr4M7Y",
            "server_id": "0341362"
        }
    ]
    models.Account.bulk_insert(items)
