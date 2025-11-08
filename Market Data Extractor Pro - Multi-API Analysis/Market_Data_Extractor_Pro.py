# En una NUEVA celda de Colab, ejecuta:
%%writefile market_extractor.py

# ====================================================================
# EXTRACTOR MASIVO DE DATOS DE MERCADO - GOOGLE COLAB VERSION
# Para cTrader Pepperstone - Análisis con Claude
# ====================================================================

# PASO 1: INSTALACIÓN DE LIBRERÍAS
print("📦 Instalando librerías necesarias...")
!pip install -q yfinance pandas requests

import yfinance as yf
import pandas as pd
import requests
import json
from datetime import datetime
import time
from google.colab import files
import io

print("✅ Librerías instaladas\n")

# ====================================================================
# CLASE PRINCIPAL
# ====================================================================

class MultiAPIMarketExtractor:
    """Extractor masivo optimizado para Google Colab"""
    
    def __init__(self):
        self.simbolos_ctrader = {
            'us_mega': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA', 'BRK-B'],
            'us_tech': ['AMD', 'INTC', 'ORCL', 'ADBE', 'CRM', 'NFLX', 'PYPL', 'UBER', 'SHOP', 'SQ',
                       'SNOW', 'PLTR', 'COIN', 'RBLX', 'ZM', 'CRWD', 'NET', 'DDOG', 'PANW'],
            'us_finance': ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'C', 'V', 'MA', 'AXP', 'SCHW',
                          'BLK', 'SPGI', 'CB', 'PGR'],
            'us_healthcare': ['JNJ', 'UNH', 'PFE', 'ABBV', 'LLY', 'MRK', 'TMO', 'ABT', 'DHR',
                             'AMGN', 'GILD', 'CVS', 'ISRG', 'VRTX'],
            'us_consumer': ['WMT', 'HD', 'MCD', 'NKE', 'SBUX', 'KO', 'PEP', 'DIS', 'COST',
                           'LOW', 'TJX', 'TGT', 'BKNG', 'ABNB'],
            'us_energy': ['XOM', 'CVX', 'COP', 'SLB', 'EOG', 'MPC', 'PSX', 'VLO', 'OXY'],
            'us_industrial': ['BA', 'CAT', 'GE', 'HON', 'UPS', 'LMT', 'RTX', 'DE', 'UNP', 'FDX'],
            'indices': ['^GSPC', '^DJI', '^IXIC', '^RUT', '^VIX'],
            'etfs': ['SPY', 'QQQ', 'IWM', 'GLD', 'SLV', 'TLT', 'HYG', 'EEM'],
            'crypto': ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'SOL-USD', 'ADA-USD'],
        }
        
        self.top_200 = self._cargar_top_200()
    
    def _cargar_top_200(self):
        """Top 200 acciones más líquidas"""
        return [
            # Mega Caps
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'BRK-B', 'LLY', 'AVGO',
            # Tech
            'AMD', 'INTC', 'ORCL', 'CRM', 'ADBE', 'NFLX', 'CSCO', 'ACN', 'TXN', 'QCOM',
            'INTU', 'IBM', 'NOW', 'AMAT', 'PANW', 'MU', 'ADI', 'LRCX', 'KLAC', 'SNPS',
            'CDNS', 'MRVL', 'FTNT', 'CRWD', 'WDAY', 'TEAM', 'DDOG', 'ZS', 'NET', 'PLTR',
            # Finance
            'JPM', 'V', 'MA', 'BAC', 'WFC', 'GS', 'MS', 'BLK', 'C', 'AXP',
            'SPGI', 'CB', 'SCHW', 'PGR', 'MMC', 'ICE', 'PNC', 'USB', 'TFC', 'COF',
            # Healthcare
            'UNH', 'JNJ', 'ABBV', 'MRK', 'TMO', 'ABT', 'DHR', 'PFE', 'AMGN', 'BMY',
            'CVS', 'ISRG', 'VRTX', 'CI', 'GILD', 'REGN', 'BSX', 'MDT', 'HUM', 'SYK',
            # Consumer
            'WMT', 'PG', 'COST', 'HD', 'KO', 'PEP', 'MCD', 'NKE', 'SBUX', 'DIS',
            'CMCSA', 'PM', 'LOW', 'TJX', 'BKNG', 'ABNB', 'MAR', 'GM', 'F', 'LULU',
            # Energy
            'XOM', 'CVX', 'COP', 'SLB', 'EOG', 'MPC', 'PSX', 'VLO', 'OXY', 'HAL',
            # Industrial
            'BA', 'CAT', 'GE', 'HON', 'UPS', 'RTX', 'LMT', 'DE', 'UNP', 'FDX',
            'MMM', 'ETN', 'EMR', 'ITW', 'CARR', 'NSC', 'PCAR', 'GD', 'CSX', 'WM',
            # Materials & Others
            'LIN', 'APD', 'SHW', 'FCX', 'ECL', 'NEM', 'CTVA', 'DD', 'NUE', 'DOW',
            # Communication
            'T', 'VZ', 'TMUS', 'CHTR', 'EA', 'TTWO', 'ATVI',
            # Utilities
            'NEE', 'SO', 'DUK', 'CEG', 'AEP', 'D', 'PEG', 'SRE', 'EXC', 'XEL',
            # Real Estate
            'PLD', 'AMT', 'EQIX', 'CCI', 'PSA', 'WELL', 'SPG', 'O', 'DLR', 'CBRE',
            # ETFs
            'SPY', 'QQQ', 'IWM', 'DIA', 'GLD', 'SLV', 'TLT', 'HYG', 'LQD', 'EEM',
            # Indices
            '^GSPC', '^DJI', '^IXIC', '^RUT', '^VIX',
        ]
    
    def obtener_datos_yahoo(self, simbolo):
        """Extrae todos los datos disponibles de Yahoo Finance"""
        try:
            ticker = yf.Ticker(simbolo)
            hist = ticker.history(period="6mo")
            
            if hist.empty:
                return None
            
            info = ticker.info
            ultimo = hist.iloc[-1]
            closes = hist['Close']
            
            # Medias móviles
            sma_20 = closes.rolling(20).mean().iloc[-1] if len(closes) >= 20 else None
            sma_50 = closes.rolling(50).mean().iloc[-1] if len(closes) >= 50 else None
            sma_200 = closes.rolling(200).mean().iloc[-1] if len(closes) >= 200 else None
            
            # RSI
            delta = closes.diff()
            gain = (delta.where(delta > 0, 0)).rolling(14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
            rs = gain / loss
            rsi = (100 - (100 / (1 + rs.iloc[-1]))) if len(closes) >= 14 else None
            
            # MACD
            ema_12 = closes.ewm(span=12).mean()
            ema_26 = closes.ewm(span=26).mean()
            macd = (ema_12 - ema_26).iloc[-1] if len(closes) >= 26 else None
            signal = (ema_12 - ema_26).ewm(span=9).mean().iloc[-1] if len(closes) >= 35 else None
            
            # Bollinger Bands
            bb_middle = closes.rolling(20).mean()
            bb_std = closes.rolling(20).std()
            bb_upper = (bb_middle + 2*bb_std).iloc[-1] if len(closes) >= 20 else None
            bb_lower = (bb_middle - 2*bb_std).iloc[-1] if len(closes) >= 20 else None
            
            # Volatilidad
            returns = closes.pct_change()
            vol_10d = returns.tail(10).std() * 100 if len(returns) > 10 else None
            vol_30d = returns.tail(30).std() * 100 if len(returns) > 30 else None
            
            # ATR
            high = hist['High']
            low = hist['Low']
            close = hist['Close'].shift(1)
            tr1 = high - low
            tr2 = abs(high - close)
            tr3 = abs(low - close)
            tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
            atr = tr.rolling(14).mean().iloc[-1] if len(tr) >= 14 else None
            
            # Cambios históricos
            cambio_1d = ((ultimo['Close'] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2] * 100) if len(hist) > 1 else None
            cambio_5d = ((ultimo['Close'] - hist['Close'].iloc[-6]) / hist['Close'].iloc[-6] * 100) if len(hist) > 5 else None
            cambio_1m = ((ultimo['Close'] - hist['Close'].iloc[-21]) / hist['Close'].iloc[-21] * 100) if len(hist) > 21 else None
            cambio_3m = ((ultimo['Close'] - hist['Close'].iloc[-63]) / hist['Close'].iloc[-63] * 100) if len(hist) > 63 else None
            
            # Volumen
            vol_promedio = hist['Volume'].tail(30).mean()
            vol_relativo = (ultimo['Volume'] / vol_promedio) if vol_promedio > 0 else None
            
            # Rangos
            max_52w = closes.tail(252).max() if len(closes) > 252 else closes.max()
            min_52w = closes.tail(252).min() if len(closes) > 252 else closes.min()
            dist_max = ((ultimo['Close'] - max_52w) / max_52w * 100)
            dist_min = ((ultimo['Close'] - min_52w) / min_52w * 100)
            
            return {
                'precio_actual': round(ultimo['Close'], 4),
                'apertura': round(ultimo['Open'], 4),
                'maximo': round(ultimo['High'], 4),
                'minimo': round(ultimo['Low'], 4),
                'volumen': int(ultimo['Volume']),
                'cambio_1d_pct': round(cambio_1d, 2) if cambio_1d else None,
                'cambio_5d_pct': round(cambio_5d, 2) if cambio_5d else None,
                'cambio_1m_pct': round(cambio_1m, 2) if cambio_1m else None,
                'cambio_3m_pct': round(cambio_3m, 2) if cambio_3m else None,
                'sma_20': round(sma_20, 4) if sma_20 else None,
                'sma_50': round(sma_50, 4) if sma_50 else None,
                'sma_200': round(sma_200, 4) if sma_200 else None,
                'rsi_14': round(rsi, 2) if rsi else None,
                'macd': round(macd, 4) if macd else None,
                'macd_signal': round(signal, 4) if signal else None,
                'bb_upper': round(bb_upper, 4) if bb_upper else None,
                'bb_lower': round(bb_lower, 4) if bb_lower else None,
                'atr_14': round(atr, 4) if atr else None,
                'volatilidad_10d': round(vol_10d, 2) if vol_10d else None,
                'volatilidad_30d': round(vol_30d, 2) if vol_30d else None,
                'volumen_promedio_30d': int(vol_promedio) if vol_promedio else None,
                'volumen_relativo': round(vol_relativo, 2) if vol_relativo else None,
                'max_52w': round(max_52w, 4),
                'min_52w': round(min_52w, 4),
                'distancia_max_52w_pct': round(dist_max, 2),
                'distancia_min_52w_pct': round(dist_min, 2),
                'market_cap': info.get('marketCap'),
                'pe_ratio': round(info.get('trailingPE', 0), 2) if info.get('trailingPE') else None,
                'forward_pe': round(info.get('forwardPE', 0), 2) if info.get('forwardPE') else None,
                'peg_ratio': round(info.get('pegRatio', 0), 2) if info.get('pegRatio') else None,
                'price_to_book': round(info.get('priceToBook', 0), 2) if info.get('priceToBook') else None,
                'dividend_yield': round(info.get('dividendYield', 0) * 100, 2) if info.get('dividendYield') else None,
                'beta': round(info.get('beta', 0), 2) if info.get('beta') else None,
                'profit_margin': round(info.get('profitMargins', 0) * 100, 2) if info.get('profitMargins') else None,
                'revenue_growth': round(info.get('revenueGrowth', 0) * 100, 2) if info.get('revenueGrowth') else None,
                'roe': round(info.get('returnOnEquity', 0) * 100, 2) if info.get('returnOnEquity') else None,
                'debt_to_equity': round(info.get('debtToEquity', 0), 2) if info.get('debtToEquity') else None,
                'nombre': info.get('longName', simbolo),
                'sector': info.get('sector', 'N/A'),
                'industria': info.get('industry', 'N/A'),
            }
        except Exception as e:
            return None
    
    def obtener_crypto_coingecko(self, simbolo):
        """Datos adicionales de crypto via CoinGecko"""
        mapping = {
            'BTC-USD': 'bitcoin', 'ETH-USD': 'ethereum', 'BNB-USD': 'binancecoin',
            'XRP-USD': 'ripple', 'SOL-USD': 'solana', 'ADA-USD': 'cardano',
        }
        
        if simbolo not in mapping:
            return {}
        
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{mapping[simbolo]}"
            response = requests.get(url, timeout=10)
            
            if response.status_code != 200:
                return {}
            
            data = response.json()
            market = data.get('market_data', {})
            
            return {
                'crypto_rank': data.get('market_cap_rank'),
                'crypto_sentiment_up': data.get('sentiment_votes_up_percentage'),
                'crypto_ath': market.get('ath', {}).get('usd'),
                'crypto_ath_change_pct': market.get('ath_change_percentage', {}).get('usd'),
                'crypto_atl': market.get('atl', {}).get('usd'),
                'crypto_circulating_supply': market.get('circulating_supply'),
            }
        except:
            return {}
    
    def extraer_todo(self, modo='rapido'):
        """Extracción masiva"""
        if modo == 'rapido':
            simbolos = (self.simbolos_ctrader['us_mega'] + 
                       self.simbolos_ctrader['indices'] + 
                       self.simbolos_ctrader['crypto'][:3])
        elif modo == 'medio':
            simbolos = []
            for cat in ['us_mega', 'us_tech', 'us_finance', 'us_healthcare', 
                       'us_consumer', 'us_energy', 'indices', 'etfs', 'crypto']:
                simbolos.extend(self.simbolos_ctrader[cat])
        else:
            simbolos = self.top_200 + self.simbolos_ctrader['crypto']
        
        simbolos = list(set(simbolos))
        
        print(f"\n{'='*80}")
        print(f"🚀 EXTRACCIÓN MASIVA - Modo: {modo.upper()}")
        print(f"{'='*80}")
        print(f"📊 Total: {len(simbolos)} símbolos")
        print(f"⏱️  Estimado: {len(simbolos) * 0.5:.0f} seg\n")
        
        datos_completos = {}
        errores = 0
        
        for i, simbolo in enumerate(simbolos, 1):
            datos = self.obtener_datos_yahoo(simbolo)
            
            if datos is None:
                errores += 1
                continue
            
            if '-USD' in simbolo:
                datos.update(self.obtener_crypto_coingecko(simbolo))
            
            datos_completos[simbolo] = datos
            
            if i % 10 == 0 or i == len(simbolos):
                print(f"✓ {i}/{len(simbolos)} ({(i/len(simbolos)*100):.0f}%) - {simbolo}")
            
            time.sleep(0.1)
        
        print(f"\n✅ Exitosos: {len(datos_completos)} | ✗ Errores: {errores}\n")
        
        return {
            'timestamp': datetime.now().isoformat(),
            'modo': modo,
            'total_simbolos': len(datos_completos),
            'datos_mercado': datos_completos,
            'metadata': {
                'fuentes': ['Yahoo Finance', 'CoinGecko'],
                'indicadores': ['RSI', 'MACD', 'BB', 'ATR', 'SMA', 'Vol', 'Fundamentales']
            }
        }
    
    def exportar(self, datos):
        """Exporta y descarga archivos"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # JSON
        json_data = json.dumps(datos, indent=2, ensure_ascii=False)
        json_filename = f'market_data_{timestamp}.json'
        
        # TXT para Claude
        txt_lines = []
        txt_lines.append("="*80)
        txt_lines.append("RAW MARKET DATA - ANÁLISIS COMPLETO")
        txt_lines.append("="*80)
        txt_lines.append(f"Timestamp: {datos['timestamp']}")
        txt_lines.append(f"Modo: {datos['modo']}")
        txt_lines.append(f"Total Símbolos: {datos['total_simbolos']}")
        txt_lines.append(f"Fuentes: {', '.join(datos['metadata']['fuentes'])}")
        txt_lines.append("="*80)
        txt_lines.append("")
        txt_lines.append("INSTRUCCIONES PARA CLAUDE:")
        txt_lines.append("-"*80)
        txt_lines.append("Analiza esta data cruda y:")
        txt_lines.append("1. Identifica patrones y anomalías")
        txt_lines.append("2. Encuentra las mejores oportunidades de trading")
        txt_lines.append("3. Dame setups específicos para cTrader (entry, SL, TP)")
        txt_lines.append("4. Considera correlaciones y contexto macro")
        txt_lines.append("5. Prioriza por risk/reward")
        txt_lines.append("="*80)
        txt_lines.append("")
        
        for simbolo, info in sorted(datos['datos_mercado'].items()):
            txt_lines.append(f"\n{'='*80}")
            txt_lines.append(f"SÍMBOLO: {simbolo}")
            txt_lines.append(f"{'='*80}")
            for key, value in info.items():
                if value is not None and value != 'N/A':
                    txt_lines.append(f"{key}: {value}")
        
        txt_content = '\n'.join(txt_lines)
        txt_filename = f'market_data_{timestamp}.txt'
        
        # Guardar archivos
        with open(json_filename, 'w', encoding='utf-8') as f:
            f.write(json_data)
        
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write(txt_content)
        
        print(f"✅ Archivos generados:")
        print(f"   📄 {txt_filename}")
        print(f"   📊 {json_filename}\n")
        
        return txt_filename, json_filename


# ====================================================================
# EJECUCIÓN PRINCIPAL
# ====================================================================

print("\n" + "="*80)
print("🎯 EXTRACTOR MASIVO MULTI-API - GOOGLE COLAB")
print("="*80)
print("\nMODOS:")
print("  1. RÁPIDO   → ~20 símbolos  | ~10 seg")
print("  2. MEDIO    → ~100 símbolos | ~50 seg")
print("  3. COMPLETO → ~200 símbolos | ~100 seg")
print("="*80 + "\n")

# Input del usuario
modo_input = input("Elige modo (1/2/3): ").strip()
modo_map = {'1': 'rapido', '2': 'medio', '3': 'completo'}
modo = modo_map.get(modo_input, 'rapido')

# Crear extractor y ejecutar
extractor = MultiAPIMarketExtractor()
print("\n🚀 Iniciando extracción...\n")
datos = extractor.extraer_todo(modo=modo)

# Exportar archivos
print("\n📝 Exportando datos...\n")
txt_file, json_file = extractor.exportar(datos)

# Descargar archivos
print("⬇️  Descargando archivos a tu PC...\n")
files.download(txt_file)
files.download(json_file)

print("\n" + "="*80)
print("✅ PROCESO COMPLETADO")
print("="*80)
print("\n📋 SIGUIENTE PASO:")
print("   1. Los archivos se descargaron a tu PC")
print("   2. Abre el archivo .txt")
print("   3. Copia TODO el contenido")
print("   4. Pégalo en tu conversación con Claude")
print("   5. Pide: 'Analiza esto como mi mentor de cTrader'")
print("\n💡 Claude analizará toda la data sin filtros previos")
print("="*80 + "\n")
