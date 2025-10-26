async function loadPrices() {
  const res = await fetch('/api/prices');
  const data = await res.json();
  const container = document.querySelector('.crypto-grid');
  container.innerHTML = '';

  for (const [symbol, info] of Object.entries(data)) {
    const changeClass = info.change >= 0 ? 'up' : 'down';
    const changeSign = info.change >= 0 ? '+' : '';
    container.innerHTML += `
      <div class="card">
        <h2>${symbol.replace('USDT', '')}</h2>
        <div class="price">$${info.price.toFixed(3)}</div>
        <div class="change ${changeClass}">${changeSign}${info.change.toFixed(2)}%</div>
      </div>
    `;
  }
}

loadPrices();
setInterval(loadPrices, 5000);
