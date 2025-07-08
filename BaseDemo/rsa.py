import hashlib
import time
from cryptography.hazmat.primitives import hashes, serialization, asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_rsa_keypair():
    """
    Generate a new RSA key pair.
    Returns the private and public keys.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_with_rsa(private_key, message) -> bytes:
    """
    Sign a message using the provided RSA private key.
    Returns the signature.
    """
    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_with_rsa(public_key, message, signature) -> bool:
    """
    Verify a signature using the provided RSA public key.
    Returns True if the signature is valid, False otherwise.
    """
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

nickname = "thneonl"
private_key, public_key = generate_rsa_keypair()
message = f"Hello, {nickname}!"
signature = sign_with_rsa(private_key, message)
is_valid = verify_with_rsa(public_key, message, signature)

print(f"Message: {message}")
print(f"\n✍ 签名 (Base64显示前20字节): {signature[:20].hex()}...")
print(f"Signature valid: {is_valid}")