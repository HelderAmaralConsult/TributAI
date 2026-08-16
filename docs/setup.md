# Configuração do Ambiente

## Ambiente Virtual Python

Criar ambiente virtual:

```bash
python3 -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

Desativar:

```bash
deactivate
```

---

## Dependências

Instalar dependências:

```bash
pip install sentence-transformers
```

---

## Configuração de Swap

Necessário para utilização do modelo de embeddings
`ulysses-camara/legal-bert-pt-br`.

### Criar arquivo de swap

```bash
sudo fallocate -l 2G /swapfile
```

### Ajustar permissões

```bash
sudo chmod 600 /swapfile
```

### Criar área de swap

```bash
sudo mkswap /swapfile
```

### Habilitar swap

```bash
sudo swapon /swapfile
```

### Persistir após reboot

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Verificar

```bash
free -h
```

Resultado esperado:

```text
Swap: 2.0Gi
```

---

## Encerrar Sessão

Sair do ambiente virtual:

```bash
deactivate
```

Fechar sessão SSH:

```bash
exit
```
