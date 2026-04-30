import json, os, sys

F = "data.json"

def ld():
    if os.path.exists(F):
        with open(F, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def sv(d):
    with open(F, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False)


def start():
    d = ld()

    if len(sys.argv) > 1:
        args = sys.argv[1:]
        inte = False
    else:
        print("add, add-category, list, total, exit")
        inte = True

    while True:
        if inte:
            inp = input("\n> ").strip().split()
            if not inp: continue
            cmd = inp[0].lower()
            par = inp[1:]
        else:
            cmd = args[0].lower()
            par = args[1:]

        if cmd == "exit": break

        if cmd == "add-category":
            c = par[0].lower()
            if c not in d:
                d[c] = []
                sv(d)
                print("сделал")
            else:
                print("уже есть")

        elif cmd == "add":
            if len(par) >= 3:
                val = float(par[0])
                c = par[1].lower()
                n = " ".join(par[2:])
                if c in d:
                    d[c].append({"n": n, "v": val})
                    sv(d)
                    print("ок")
                else:
                    print("нет такой категории")

        elif cmd == "list":
            c = par[0].lower() if par else None
            if c and c in d:
                for x in d[c]: print(f"{x['n']}: {x['v']}")
            else:
                for k in d: print(f"{k}: {sum(i['v'] for i in d[k])}")
        elif cmd == "total":
            c = par[0].lower() if par else None
            if c and c in d:
                print(sum(i["v"] for i in d[c]))
            else:
                s = 0
                for k in d: s += sum(i["v"] for i in d[k])
                print("всего:", s)
        if not inte: break
start()
