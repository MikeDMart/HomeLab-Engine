# 📊 Market Data Extractor Pro - Multi-API Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-orange?logo=googlecolab)
![API](https://img.shields.io/badge/API-Yahoo%20Finance%20%7C%20CoinGecko-green)
![Trading](https://img.shields.io/badge/Trading-cTrader%20Ready-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Extractor masivo de datos financieros para análisis avanzado en cTrader**

*Extrae, procesa y analiza +200 instrumentos en segundos*

</div>

## 🚀 Características Principales

### 📈 Análisis Técnico Completo
- **Indicadores Avanzados**: RSI, MACD, Bollinger Bands, ATR, Medias Móviles
- **Volatilidad**: Cálculo de volatilidad histórica (10D, 30D)
- **Volumen**: Análisis de volumen relativo y promedios
- **Rangos**: Distancias desde máximos/mínimos 52 semanas

### 💰 Datos Fundamentales
- **Métricas Clave**: P/E, P/B, PEG Ratio, Dividend Yield
- **Crecimiento**: Revenue Growth, Profit Margins, ROE
- **Deuda**: Debt-to-Equity, Beta del mercado
- **Capitalización**: Market Cap y ranking sectorial

### 🌐 Multi-Fuente de Datos
- **Yahoo Finance**: +200 acciones, ETFs, índices
- **CoinGecko**: Datos cripto en tiempo real
- **cTrader Optimized**: Símbolos compatibles con Pepperstone

## 🎯 Modos de Operación

| Modo | Símbolos | Tiempo | Uso Recomendado |
|------|----------|---------|-----------------|
| 🚀 **Rápido** | ~20 | 10 seg | Análisis rápido |
| ⚡ **Medio** | ~100 | 50 seg | Trading diario |
| 🔥 **Completo** | ~200+ | 100 seg | Análisis profundo |

## 📊 Instrumentos Cubiertos

### 🏢 Acciones por Sector

sectores = {
    'Tecnología': ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'META', 'AMD', 'INTC'],
    'Finanzas': ['JPM', 'V', 'MA', 'BAC', 'GS', 'MS'],
    'Salud': ['JNJ', 'UNH', 'PFE', 'ABBV', 'LLY', 'MRK'],
    'Consumo': ['WMT', 'HD', 'MCD', 'NKE', 'SBUX', 'KO'],
    'Energía': ['XOM', 'CVX', 'COP', 'SLB', 'EOG'],
    'Industrial': ['BA', 'CAT', 'GE', 'HON', 'UPS']
}

📈 Índices & ETFs

indices = ['^GSPC', '^DJI', '^IXIC', '^RUT', '^VIX']
etfs = ['SPY', 'QQQ', 'IWM', 'GLD', 'SLV', 'TLT']
₿ Criptomonedas
python
cripto = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'SOL-USD', 'ADA-USD']


🛠️ Instalación Rápida
Google Colab (Recomendado)

# Copia y pega este código en una celda de Colab
!git clone https://github.com/MikeDMart/HomeLab-Engine.git
%cd HomeLab-Engine/yfinance-api

# Ejecuta el extractor
!python market_extractor.py
Opción Directa en Colab
python
# Ejecuta directamente sin clonar
from google.colab import drive
drive.mount('/content/drive')

# Copia el código del extractor y ejecuta
📋 Uso Paso a Paso
1. Ejecutar en Colab
python
# El script pregunta por el modo deseado
🎯 EXTRACTOR MASIVO MULTI-API - GOOGLE COLAB
=================================================

MODOS:
  1. RÁPIDO   → ~20 símbolos  | ~10 seg
  2. MEDIO    → ~100 símbolos | ~50 seg
  3. COMPLETO → ~200 símbolos | ~100 seg

Elige modo (1/2/3): 2
2. Extracción Automática
python
🚀 EXTRACCIÓN MASIVA - Modo: MEDIO
=================================================
📊 Total: 98 símbolos
⏱️  Estimado: 49 seg

✓ 10/98 (10%) - AAPL
✓ 20/98 (20%) - MSFT
✓ 30/98 (31%) - GOOGL
...
✅ Exitosos: 95 | ✗ Errores: 3
3. Exportación de Resultados
python
📝 Exportando datos...

✅ Archivos generados:
   📄 market_data_20241215_143022.txt
   📊 market_data_20241215_143022.json

⬇️  Descargando archivos a tu PC...
4. Análisis con Claude AI
text
📋 SIGUIENTE PASO:
   1. Los archivos se descargaron a tu PC
   2. Abre el archivo .txt
   3. Copia TODO el contenido
   4. Pégalo en tu conversación con Claude
   5. Pide: 'Analiza esto como mi mentor de cTrader'
📊 Ejemplo de Salida
Archivo TXT (Para Claude AI)
text
================================================================================
RAW MARKET DATA - ANÁLISIS COMPLETO
================================================================================
Timestamp: 2024-12-15T14:30:22.123456
Modo: medio
Total Símbolos: 95
Fuentes: Yahoo Finance, CoinGecko
================================================================================

INSTRUCCIONES PARA CLAUDE:
--------------------------------------------------------------------------------
Analiza esta data cruda y:
1. Identifica patrones y anomalías
2. Encuentra las mejores oportunidades de trading
3. Dame setups específicos para cTrader (entry, SL, TP)
4. Considera correlaciones y contexto macro
5. Prioriza por risk/reward
================================================================================

SÍMBOLO: AAPL
================================================================================
precio_actual: 185.25
apertura: 184.50
maximo: 186.75
minimo: 183.80
volumen: 58425000
cambio_1d_pct: 1.25
sma_20: 182.45
sma_50: 178.90
rsi_14: 58.3
macd: 0.45
volatilidad_30d: 2.45
market_cap: 2850000000000
pe_ratio: 28.5
Archivo JSON (Para Desarrollo)
json
{
  "timestamp": "2024-12-15T14:30:22.123456",
  "modo": "medio",
  "total_simbolos": 95,
  "datos_mercado": {
    "AAPL": {
      "precio_actual": 185.25,
      "apertura": 184.5,
      "rsi_14": 58.3,
      "macd": 0.45
    }
  }
}


🎨 Visualización de Datos
El extractor incluye análisis visual automático:

Gráficos de tendencia con medias móviles

Análisis RSI para sobrecompra/sobreventa

Bandas de Bollinger para volatilidad

Comparativa sectorial para rotación

🔧 Personalización
Configurar Símbolos Personalizados
python
# Modifica la clase para agregar tus símbolos
class MiExtractorPersonalizado(MultiAPIMarketExtractor):
    def __init__(self):
        super().__init__()
        self.simbolos_ctrader['mis_symbols'] = ['MISIMBOLO1', 'MISIMBOLO2']
Agregar Nuevos Indicadores
python
def calcular_indicador_personalizado(self, datos):
    # Tu lógica personalizada aquí
    return indicador_personalizado
📈 Casos de Uso
🎯 Para Traders
Swing Trading: Identificar setups con RSI + MACD

Day Trading: Análisis de volumen y volatilidad

Position Trading: Fundamentales + tendencias largas

🔬 Para Analistas
Análisis Sectorial: Comparativa entre sectores

Correlaciones: Identificar relaciones entre activos

Backtesting: Datos históricos para estrategias

🤖 Para Desarrolladores
APIs: Base para sistemas automáticos

Machine Learning: Datos para modelos predictivos

Dashboards: Fuente para visualizaciones

🚨 Características de Seguridad
✅ Rate Limiting: Protección contra bans de API

✅ Manejo de Errores: Continuación tras fallos

✅ Timeouts: Protección contra respuestas lentas

✅ Validación: Verificación de datos recibidos

📊 Métricas de Rendimiento
Operación	Tiempo Promedio	Confiabilidad
Extracción símbolo	0.5s	98%
Procesamiento datos	0.1s	99%
Exportación	2s	100%
Total (200 símbolos)	~100s	97%
🤝 Contribución
¡Contribuciones son bienvenidas!

Fork el proyecto

Crea una rama (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

Mejoras Planeadas
Integración con más APIs financieras

Análisis técnico avanzado

Alertas automáticas

Dashboard web integrado

📄 Licencia
Distribuido bajo licencia MIT. Ver LICENSE para más información.

⚠️ Disclaimer
NOTA IMPORTANTE: Este software es para análisis educativo y de investigación. No constituye consejo de inversión. El trading conlleva riesgos significativos y puede resultar en la pérdida de tu capital.

<div align="center">
¿Te gusta este proyecto? ⭐ Dale una estrella en GitHub!
Desarrollado con ❤️ para la comunidad de trading

📧 Reportar Issue •
💡 Sugerir Feature •
🔄 Actualizaciones

</div> ```
