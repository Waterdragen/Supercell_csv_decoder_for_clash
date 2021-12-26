First, generate 2 folders by running main.py

In-csv			----Put your packed/encoded .csv here
Out-csv			----Get your decoded .csv here
keyword.txt		----The header you want to keep (binary data) which is ]
csv_decoder.py	----Run the program and it will get all .csv in In-csv and you get all the
				decoded .csv in Out-csv

Sample output:
Here are your .csv files:

3d_environment.csv                  ---- Decode
animations.csv                      ---- Decode
buildings.csv                       ---- OK
chat_rules.csv                      ---- Decode
client_globals.csv                  ---- Trim+Decode
credits.csv                         ---- Decode
resource_packs.csv                  ---- Decode
skins.csv                           ---- Trim+Decode
skin_projectile_vis.csv             ---- Decode
spells.csv                          ---- Trim+Decode
townhall_levels.csv                 ---- Trim+Decode
trader.csv                          ---- Trim+Decode
traps.csv                           ---- Trim+Decode

Decoded .csv saved to Out-csv
Press Enter to exit

decode_file() credits: proydakov's supercell_resource_decoder

By Waterdragen @Orbit 2021
