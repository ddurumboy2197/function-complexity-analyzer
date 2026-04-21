import threading
import queue
import time
import random

# Producer funksiyasi
def producer(q, name):
    for i in range(10):
        item = f"Item {i}"
        q.put(item)
        print(f"{name} sent: {item}")
        time.sleep(random.uniform(0.1, 0.5))

# Consumer funksiyasi
def consumer(q, name):
    for _ in range(10):
        item = q.get()
        print(f"{name} received: {item}")
        time.sleep(random.uniform(0.1, 0.5))
        q.task_done()

# Main funksiya
def main():
    q = queue.Queue()

    # Producer threadlar yaratish
    producer_threads = []
    for i in range(3):
        t = threading.Thread(target=producer, args=(q, f"Producer {i+1}"))
        t.start()
        producer_threads.append(t)

    # Consumer threadlar yaratish
    consumer_threads = []
    for i in range(2):
        t = threading.Thread(target=consumer, args=(q, f"Consumer {i+1}"))
        t.start()
        consumer_threads.append(t)

    # Producer threadlar tugashini kutish
    for t in producer_threads:
        t.join()

    # Consumer threadlar tugashini kutish
    for t in consumer_threads:
        t.join()

    # Queue tugashini kutish
    q.join()

if __name__ == "__main__":
    main()
```

Kodda quyidagilar amalga oshirildi:

1.  Producer va Consumer funksiyalari yaratildi, ular quyidagilarni amalga oshiradi:
    *   Producer: Queuega itemlarni qo'yadi.
    *   Consumer: Queuedan itemlarni olib, ularni konsolga chiqaradi.
2.  Main funksiyasi yaratildi, u quyidagilarni amalga oshiradi:
    *   Queue yaratildi.
    *   3 ta Producer va 2 ta Consumer threadlari yaratildi.
    *   Producer threadlari tugashini kutadi.
    *   Consumer threadlari tugashini kutadi.
    *   Queue tugashini kutadi.
3.  Main funksiyasi boshlanadi, agar skriptni ishga tushirishda muammolar bo'lsa, u quyidagi kodni boshqa skriptda bajaradi: `if __name__ == "__main__":`
