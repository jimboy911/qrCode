QR Code Generator
Setup Process

python3 -m venv qr_venv <<<< creates venv folder
source qr_venv/bin/activate <<<< jumps into virtual environment in macOS
pip install "qrcode[pil]" <<< this installs qrcode into your environment

------

20240126 - it works!
    ask user to type in website and have it generate a qr code for that > done
    timestamp the qr code file > done

---------

20240127 - Next:    
    turn it into a flask app
