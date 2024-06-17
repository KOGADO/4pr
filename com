geth account new --datadir data - создание нового аккаунта
geth init -datadir data genesis.json - создание генезис блока

geth --datadir data --networkid 234 --unlock  0x2013f636aC331618A8bcd5CfBD23637D5EC7d15A --allow-insecure-unlock --http --http.corsdomain="*" --http.api web3,eth,debug,personal,net,miner --miner.etherbase 0x2013f636aC331618A8bcd5CfBD23637D5EC7d15A - запуск чатсной сети блокчейна
geth attach --datadir data ipc:\\.\pipe\geth.ipc - создание отдельной консоли geth для того, чтобы управлять процессами в блокчейне
    eth.blockNumber - номер блока



0x2013f636aC331618A8bcd5CfBD23637D5EC7d15A
0x58a7a37fd21bd6b35cA95eeF6148efe6FD1b7352
0x3CFeaB84b97539a656F3C0c1b056B35896C72a6c
0xf973DeE15922C6E22E4fDA2BC50CB4e687d5f36A
0xda08117960603651B84a194790098d250844a3cF