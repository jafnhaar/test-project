# test-project

1. Что необходимо сделать?
   - упаковать данный проект в контейнер;
   - размер конечного image не должен превышать 200МБ;
   - написать helm chart;
2. Helm chart
   
    Результирующий Helm Chart должен включать в себя следующие API объекты:
      - deployment;
      - ingress;
      - service;
      - servicemonitors.monitoring.coreos.com;
      - cronjob;
      - для объекта ingress должна быть возможность использовать cert-manager для генерации HTTPS сертефикатов от Let's Encrypt; Представим, что текущий ClusterIssuer называется letsencrypt.
3. Вводные данные о приложении

Поддерживает следующие ENV для конфигурации:


| env_name | default_value | description            | required |
| -------- | ------------- | ---------------------- | -------- |
| APP_HOST |               | default listen address | true     |
| APP_PORT |               | default listen port    | true     |
