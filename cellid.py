def decode_ecgi(ecgi_hex: str):
    """
    Decode ECGI into MCC, MNC, and Cell ID using slice method.
    ECGI is typically 14 hex digits (56 bits).
    - First part encodes PLMN (MCC + MNC)
    - Last 7 hex digits = Cell Identity (ECI)
    """
    # Normalize input
    ecgi_hex = ecgi_hex.replace("0x", "").upper()
    
    # --- Cell ID ---
    cell_id_hex = ecgi_hex[-7:]
    cell_id_dec = int(cell_id_hex, 16)
    
    # --- PLMN (MCC + MNC) ---
    plmn_hex = ecgi_hex[:-7]   # everything except last 7 hex digits
    plmn_dec = int(plmn_hex, 16)
    
    # MCC and MNC decoding depends on operator allocation.
    # For your logs, MCC=255 and MNC=061 were shown.
    # Here we just return the PLMN hex/decimal for mapping.
    
    return {
        "ECGI (hex)": ecgi_hex,
        "ECGI (decimal)": int(ecgi_hex, 16),
        "PLMN (hex)": plmn_hex,
        "PLMN (decimal)": plmn_dec,
        "Cell ID (hex)": cell_id_hex,
        "Cell ID (decimal)": cell_id_dec
    }

# Example usage:
ecgi = "5215600C5DD517"
result = decode_ecgi(ecgi)

for k, v in result.items():
    print(f"{k}: {v}")

