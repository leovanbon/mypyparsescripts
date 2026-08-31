curl -sv --max-time 15 -X POST http://154.57.164.73:32581/enum \
  -H "Host: g4m3l0ad3r-network.htb" \
  -H "Content-Type: application/json" \
  -d '{"os_name":"Windows","processor_name":"Intel Core i7","cpu_cores":8,"is_64bit":true,"locale":"en_US","user_dir":"C:/Users/user"}' 2>&1

curl -sv --max-time 15 http://154.57.164.73:32581/p47l0ad_binary \
  -H "Host: g4m3l0ad3r-network.htb" 2>&1

curl -sv --max-time 15 http://154.57.164.73:32581/p47l0ad_binary \
  -H "Host: g4m3l0ad3r-network.htb" \
  -H "Cookie: 57151533199105491179012282116775011911989878112290122821167750119119" 2>&1