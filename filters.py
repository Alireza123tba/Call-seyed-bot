import datetime
from core.config import Config

def filter_tokens(tokens):
    filtered = []
    now = datetime.datetime.utcnow()

    for token in tokens:
        try:
            mc = token.get('market_cap', 0)
            vol = token.get('volume_24h', 0)
            launched_at = datetime.datetime.strptime(token.get('launched_at'), "%Y-%m-%dT%H:%M:%SZ")
            age_minutes = (now - launched_at).total_seconds() / 60

            if mc >= Config.MIN_MARKET_CAP and vol >= Config.MIN_VOLUME_24H and age_minutes <= Config.MAX_AGE_MINUTES:
                if token.get('dex') == Config.TARGET_DEX:
                    filtered.append(token)
        except Exception:
            continue
    return filtered
