
<div align="center">
    <h1>SpeakGPT</h1>
    <p><strong>SpeakGPT</strong> é um projeto Python que interage com o ChatGPT usando Selenium para web scraping e também incorpora reconhecimento de voz para entrada do usuário.</p>
</div>

## Requisitos

- **Python**: Versão 3.6 ou superior.
- **Bibliotecas Python**:
  - `Selenium`: 
  - `pyttsx3` (BeautifulSoup4): Para parsing de HTML.
  - `speech_recognition`: Para estilização de texto no terminal.
  - Você também precisará baixar o `driver` do navegador adequado para o Selenium. Neste caso, foi utilizado o Microsoft Edge, então você precisa do `msedgedriver.exe`.


## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

1. Certifique-se de ter o driver do navegador na pasta do projeto.
2. Execute o script `SpeakGPT.py`.
3. O programa abrirá uma janela do navegador e começará a interagir com o ChatGPT.
4. Isso irá criar um novo perfil no navegador, faca login em uma conta do ChatGPT para burlar a validacao de segurança do ChatGPT.
5. Você pode fazer perguntas ao ChatGPT falando em voz alta.

## Contribuições

Contribuições para melhorar GitBrowse são sempre bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie um novo branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Desenvolva e teste suas mudanças.
4. Envie um pull request:
   ```bash
   git push origin minha-feature
   ```

## Apoio

Para apoiar o desenvolvimento contínuo e melhorias, considere tornar-se um patrocinador no Patreon:
[![Apoie no Patreon](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://patreon.com/SimpleDioney)

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
