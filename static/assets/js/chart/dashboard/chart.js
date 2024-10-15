document.addEventListener('DOMContentLoaded', function() {
  fetch('/admin_panel/chart_dashboard/get_total_items_orders/')
      .then(response => response.json())
      .then(data => {
          const ctx = document.getElementById('myChartBarOrder').getContext('2d');
          document.getElementById('TotalOrdersCant').innerText=data.total_orders;
          document.getElementById('TotalOrdersStartDay').innerText=data.data.labels[0];
          document.getElementById('TotalOrdersEndDay').innerText=data.data.labels[6];
          document.getElementById('TotalOrdersStartMonth').innerText=data.start_month;
          document.getElementById('TotalOrdersEndMonth').innerText=data.end_month;
          new Chart(ctx, {
              type: 'bar',
              data: {
                  labels: data.data.labels,
                  datasets: [{
                      label: data.title,
                      data: data.data.datasets[0].data,
                      
                  }]
              },
              options: {
                      responsive:true,
                      scales: {
                        y: {
                          beginAtZero: true
                        }
                      }
                    }
          });
      })
      .catch(error => console.error('Error:', error));
});

document.addEventListener('DOMContentLoaded', function() {
  fetch('/admin_panel/chart_dashboard/get_total_price_orders/')
      .then(response => response.json())
      .then(data => {
          const ctx = document.getElementById('myChartLineSales').getContext('2d');
          document.getElementById('TotalSalesOrdersPrice').innerText=data.total_price_orders;
          document.getElementById('TotalSalesOrdersStartDay').innerText=data.data.labels[0];
          document.getElementById('TotalSalesOrdersEndDay').innerText=data.data.labels[6];
          document.getElementById('TotalSalesOrdersStartMonth').innerText=data.start_month;
          document.getElementById('TotalSalesOrdersEndMonth').innerText=data.end_month;
          
          new Chart(ctx, {
              type: 'line',
              data: {
                  labels: data.data.labels,
                  datasets: [{
                      label: data.title,
                      data: data.data.datasets[0].data,
                      borderWidth: 1
                  }]
              },
              options: {
             
                responsive:true,
                scales: {
                  y: {
                    beginAtZero: true
                  }
                }
              }
          });
      })
      .catch(error => console.error('Error:', error));
});