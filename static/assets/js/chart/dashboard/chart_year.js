
let input = document.getElementById('dateYearDashboardChart')
let chartBarInstance = null;
let chartLineInstance = null;


input.addEventListener('change', function() {
    if (chartBarInstance) {
        chartBarInstance.destroy();
    }
    if (chartLineInstance) {
        chartLineInstance.destroy();
    }
    loadChartBar();
    loadChartLine();
  });


document.addEventListener('DOMContentLoaded', function() {
    
    loadChartBar();
    loadChartLine();
  });




function loadChartBar() {
    const year = document.getElementById('dateYearDashboardChart').value;
    fetch(`/admin_panel/chart_dashboard/get_total_items_orders_month/${year}/`)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('myChartBarOrderYearDashboard').getContext('2d');
            document.getElementById('TotalSalesOrdersCantMonth').innerText=data.total_items
            if (ctx) {
                chartBarInstance = new Chart(ctx, {
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
            }
            
        })
        .catch(error => console.error('Error:', error));
};

function loadChartLine() {
    
        const year = document.getElementById('dateYearDashboardChart').value;
        fetch(`/admin_panel/chart_dashboard/get_total_items_orders_price_month/${year}/`)
            .then(response => response.json())
            .then(data => {
                
                const ctx2 = document.getElementById('myChartLineOrderPriceYearDashboard').getContext('2d');
                document.getElementById('TotalSalesOrdersPriceMonth').innerText=data.total_price
                if (ctx2) {
                    chartLineInstance = new Chart(ctx2, {
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
                }
                
            })
            .catch(error => console.error('Error:', error));

};