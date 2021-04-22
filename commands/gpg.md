## GPG
1. `--full-gen-key` - инициализация аккаунта (1-4096-0)
2.  create `~/.gunpg/gpg.conf` by 
`echo "keyid-format 0xlong
throw-keyids
no-emit-version
no-comments" > ~/.gnupg/gpg.conf`
3. `-k` - публичные ключи
4. `-K` - приватные ключи
5. `--export -a [email] > [pub].gpg` - экспорт публичных ключей в ascii
6. `--export-secret-key` ...
7. `--delete-secret-keys [email` - удаление секретных ключей
8. `--delete-keys [email] - удаление публичных ключей (сначала нужно удалить секретные)
9. `--import [filename].pgp` - импорт новых ключей
