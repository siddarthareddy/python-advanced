import datetime
import colorama
import random
import time


def main():
    # create asyncio event loop
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    # use better data structure than list which can allow us to break up the work ..
    # like yield control back to calling function on the data structure,
    # so that say a put() is called, on yield, execution can go another call which is awaiting on
    # consuming the data put into it, which was awaiting on it
    data = []

    # convert functions below to
    # run them with asyncio.gather()
    generate_data(10, data)
    generate_data(10, data)
    process_data(20, data)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


# convert it to be executed with asyncio
# mark it as async, await at time taking call
def generate_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx*idx
        data.append((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + " -- generated item {}".format(idx), flush=True)
        time.sleep(random.random() + .5)


def process_data(num: int, data: list):
    processed = 0
    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        time.sleep(.5)


if __name__ == '__main__':
    main()
