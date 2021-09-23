import browserhistory as bh

history = bh.get_browserhistory()
bh.write_browserhistory_csv()

for browser_name,history_list in history.items():
    for tuple in history_list:
        print(f"""Address : " {tuple[0]} Name {tuple[1]} Date: {tuple[2]}""")
