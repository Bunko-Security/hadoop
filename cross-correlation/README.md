***Запускать скрипты строго из данной директории!***

Разрешить скрипту выполнение:
```bash
chmod +x ./pre-start.sh
```

После запустить сам скрипт:
```bash
./pre-start.sh
```

Для запуска алгоритма Cross Correlation Pairs:
```bash
./start-pairs.sh
```

Для запуска алгоритма Cross Correlation Stripes:
```bash
./start-stripes.sh
```

Если нужно по новой создать директории в HDFS, то выполняем:
```bash
./createdirs.sh
```