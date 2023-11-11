import marshal, base64, os, zlib, typer
from getpass import getpass  # Use getpass to securely input passphrase
from cryptography.fernet import Fernet
import sys
from io import StringIO
from uncompyle6 import deparse_code2str
from pyhide import __app_name__, __version__
from typing import Optional
import hashlib

app = typer.Typer()

# Helper Functions
def encrypt_and_serialize(code):
    obfuscated_code = compile(code, '<string>', 'exec')
    obfuscated_data = zlib.compress(marshal.dumps(obfuscated_code))
    fernet_key = Fernet.generate_key()
    cipher = Fernet(fernet_key)
    encrypted_code = cipher.encrypt(obfuscated_data)
    encrypted_data = fernet_key + encrypted_code
    return base64.b64encode(encrypted_data)

def decrypt_and_deserialize(encrypted_data):
    fernet_key = encrypted_data[:44]
    encrypted_code = encrypted_data[44:]
    cipher = Fernet(fernet_key)
    decrypted_code = cipher.decrypt(encrypted_code)
    decompressed_code = zlib.decompress(decrypted_code)
    code_object = marshal.loads(decompressed_code)
    return code_object

def eval_with_output(code):
    tmp = sys.stdout
    obf_code = StringIO()
    sys.stdout = obf_code
    eval(code)
    sys.stdout = tmp
    return obf_code

def error_message(message: str):
    return typer.style(message, fg=typer.colors.RED, bold=True)

def success_message(message: str):
    return typer.style(message, fg=typer.colors.GREEN, bold=True)

@app.command(help="Obfuscate a source file")
def obfuscate(
    input_file: str = typer.Argument(help="Full Path to the Source code file (.py)"), 
    output_file: str = typer.Argument(help="Full Path for obfuscated code file (.py)")
    ):
    try:
        passphrase = typer.prompt('Enter passphrase for de-obfuscation: ', hide_input=True)
        with open(input_file, 'r') as file:
            original_code = file.read()
        encrypted_code = encrypt_and_serialize(original_code)
        obfuscated_code_str = f"""import zlib,base64,marshal;from cryptography.fernet import Fernet;cipher = Fernet(base64.b64decode("{encrypted_code.decode()}")[:44]);decrypted_code = marshal.loads(zlib.decompress(cipher.decrypt(base64.b64decode("{encrypted_code.decode()}")[44:])));exec(decrypted_code)"""
        exec_file = f"""# {hashlib.sha512(repr(passphrase).encode()).hexdigest()}
exec("import zlib,base64;code = zlib.decompress(base64.b64decode('{base64.b64encode(zlib.compress(obfuscated_code_str.encode())).decode()}'));exec(code)")
"""
        with open(output_file, 'w') as file:
            file.write(exec_file)
        typer.echo(success_message(f'Code obfuscated and saved to {output_file}\nOriginal File Size: {os.stat(input_file).st_size} Bytes\nObfuscated File Size: {os.stat(output_file).st_size} Bytes\n'), color=True)
    except Exception as e:
        typer.echo(error_message(f'Error obfuscating code: {e}'), err=True, color=True)
        raise typer.Exit(1)

@app.command(help="De-obfuscate a file and save it to the specified output file")
def deobfuscate(
    input_file: str = typer.Argument(help="Full Path to obfuscated file"), 
    output_file: str = typer.Argument(help="Full Path to save de-obfuscated file")
    ):
    try:
        passphrase = typer.prompt('Enter passphrase for de-obfuscation ', hide_input=True)
        with open(input_file, 'r') as file:
            fdata = file.readlines()
            passphrase_hash = fdata[0].split(' ')[1].strip()
            encrypted_code = fdata[1][:-13]+"print(code)\")"
        given_passphrase_hash = hashlib.sha512(repr(passphrase).encode()).hexdigest()
        if passphrase_hash != given_passphrase_hash:
            typer.echo(error_message("Passphrase is incorrect!"), err=True, color=True)
            raise typer.Exit(1)
        
        obf_code = eval_with_output(encrypted_code)
        obf_code = obf_code.getvalue()[2:-2][:-20]
        code = obf_code.split("base64.b64decode(\"")[1].split("\")[:44]);decrypted_code")[0]
        decrypted_code = decrypt_and_deserialize(base64.b64decode(code))
        source_code = deparse_code2str(decrypted_code, out=StringIO())
        with open(output_file, 'w') as file:
            file.write(source_code)
        typer.echo(success_message(f'Code de-obfuscated and saved to {output_file}'), color=True)
    except Exception as e:
        typer.echo(error_message(f'Error de-obfuscating code: {e}'), err=True, color=True)
        raise typer.Exit(1)

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the Application's version and exit",
            callback=_version_callback,
            is_eager=True
        )
) -> None:
    return