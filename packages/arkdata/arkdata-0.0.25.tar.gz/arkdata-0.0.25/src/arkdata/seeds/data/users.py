from arkdata import models


def seed():
    items = [
        {
            "xuid": "123",
            "gamertag": "zed3kiah",
            "password_digest": "password",
            "authentication_token": "G05BeO6H6h2UMcie",
            "authenticated": False,
            "discord_username": "zed3kiah"
        },
        {
            "xuid": "02670680",
            "gamertag": "Reba",
            "password_digest": "amqAZmrd",
            "authentication_token": "G05BeO6H6h2UMcie",
            "authenticated": False,
            "discord_username": "rlefeuvre0"
        },
        {
            "xuid": "32469606",
            "gamertag": "Benji",
            "password_digest": "LyDei5bwO",
            "authentication_token": "qcCB9cJeVQ5M9DGf",
            "authenticated": True,
            "discord_username": "bvanross1"
        },
        {
            "xuid": "37694979",
            "gamertag": "Roxi",
            "password_digest": "sZFJkzR",
            "authentication_token": "uR51jLixq2eQ9HPX",
            "authenticated": True,
            "discord_username": "rfillis2"
        },
        {
            "xuid": "05203671",
            "gamertag": "Leta",
            "password_digest": "M5pa1Lkiu",
            "authentication_token": "GNcNISdGq1ss2BUo",
            "authenticated": False,
            "discord_username": "ltreverton3"
        },
        {
            "xuid": "14131099",
            "gamertag": "Kym",
            "password_digest": "qtfxhVGC3Iy",
            "authentication_token": "rNKLhkKo20kdFeh3",
            "authenticated": True,
            "discord_username": "kabelovitz4"
        },
        {
            "xuid": "46610162",
            "gamertag": "Louie",
            "password_digest": "SdY6ZrBf",
            "authentication_token": "M4tOWSfKuVO3djuY",
            "authenticated": False,
            "discord_username": "ldinis8"
        },
        {
            "xuid": "82588774",
            "gamertag": "Alvan",
            "password_digest": "nBJgRu",
            "authentication_token": "855gzGCKxt0gJ4xw",
            "authenticated": False,
            "discord_username": "astonard9"
        },
        {
            "xuid": "83510641",
            "gamertag": "Felic",
            "password_digest": "Hl0xFy",
            "authentication_token": "ZGehAFYWWd0zIluA",
            "authenticated": False,
            "discord_username": "ffrontczaka"
        },
        {
            "xuid": "92939552",
            "gamertag": "Timi",
            "password_digest": "oohWA0",
            "authentication_token": "0wzjlMthPRvK5EZZ",
            "authenticated": False,
            "discord_username": "tbrinklerd"
        },
        {
            "xuid": "76506392",
            "gamertag": "Janey",
            "password_digest": "DW0SYY",
            "authentication_token": "iDUzvJ4ZrjsyDCwn",
            "authenticated": True,
            "discord_username": "jobernf"
        },
        {
            "xuid": "09897611",
            "gamertag": "Thea",
            "password_digest": "0BhlfN49",
            "authentication_token": "dC2MkhPWQXFaPIye",
            "authenticated": False,
            "discord_username": "tkitchingmang"
        },
        {
            "xuid": "80058538",
            "gamertag": "Kellen",
            "password_digest": "5Oe8KMu",
            "authentication_token": "4cNWwW7uq1Dv6TMu",
            "authenticated": True,
            "discord_username": "kstatej"
        }
    ]
    models.User.bulk_insert(items)
