import sys
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--coin', type=str, required=True, help='coin')
    args = parser.parse_args()
    print(args.coin)

# (base) dengwei@RMBAP:~/projects/work/trading/wade/grid/stra-grid$ python a.py -c='eos'
# eos
# (base) dengwei@RMBAP:~/projects/work/trading/wade/grid/stra-grid$ python a.py -c 'eos'
# eos
# (base) dengwei@RMBAP:~/projects/work/trading/wade/grid/stra-grid$ python a.py --coin 'eos'
# eos
# (base) dengwei@RMBAP:~/projects/work/trading/wade/grid/stra-grid$ python a.py --coin='eos'
# eos