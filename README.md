# breadth_first_search_pythonn

# Breadth First Search (BFS) Algoritması

Bu proje, Python dilinde Breadth First Search (BFS) algoritmasının bir örneğini içermektedir. Algoritma, bir graf üzerinde genişlik öncelikli arama gerçekleştirir.

## Algoritma Açıklaması

- Proje, "black", "white" ve "gray" olmak üzere üç farklı renk kullanarak düğümlerin durumlarını belirtir.
- BFS algoritmasının çalışması şu adımlarla özetlenebilir:
    1. Başlangıç düğümü gri olarak işaretlenir ve kuyruğa eklenir.
    2. Kuyruk boşalmadığı sürece aşağıdaki adımlar tekrarlanır:
        - Kuyruktan bir düğüm çıkarılır ve üzerinde işlemler yapılır.
        - Çıkarılan düğümün komşuları kontrol edilir.
        - Komşular daha önce ziyaret edilmemişse gri olarak işaretlenir ve kuyruğa eklenir.
        - İşlenen düğüm siyah olarak işaretlenir.
    3. Tüm düğümler ziyaret edildiğinde BFS işlemi tamamlanır.

## Kullanım

Bu Python kodunu çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. `math` modülünü projenize dahil edin. Bu modül, matematiksel işlemler için kullanılır.
2. Kodu kopyalayın ve Python ortamında çalıştırın.
3. Örnek graf yapısını değiştirmek için `G` değişkenini güncelleyebilirsiniz. Bu graf, anahtar-değer çiftleri kullanarak temsil edilmektedir. Anahtarlar düğümleri, değerler ise düğümlerin komşu düğümlerini temsil eder.
4. `Point` sınıfı, düğüm nesnelerini tanımlamak için kullanılır. İhtiyaçlarınıza göre bu sınıfı özelleştirebilirsiniz.
5. `colors` sözlüğü, düğüm durumlarını belirlemek için renklerin RGB değerlerini içerir. Bu renkleri ihtiyaçlarınıza göre düzenleyebilirsiniz.
6. Kodu çalıştırın ve BFS algoritmasının çıktısını gözlemleyin.


## Örnek Çıktı

Breadfirst:
5 3 7 2 4 8


Bu çıktı, BFS algoritmasının "5" düğümünden başlayarak genişlik öncelikli olarak diğer düğümleri ziyaret ettiğini gösterir.

---
