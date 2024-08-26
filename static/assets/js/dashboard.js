/* globals Chart:false */
const myChartBar = document.getElementById('myChartBar');
      if (myChartBar) {
        new Chart(myChartBar, {
          type: 'bar',
          data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [{
              label: 'total sold',
              data: [120,100,150,130, 49, 123,120,160,220,190, 229, 340],
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
        
        const myChartLine = document.getElementById('myChartLine');
        if (myChartLine) {
          new Chart(myChartLine, {
            type: 'line',
            data: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December'],
              datasets: [{
                label: 'total sold',
                data: [120,100,150,130, 49, 123,120,160,220,190, 229, 340],
                borderWidth: 1
              }]
            },
            options: {
              animations: {
                tension: {
                  duration: 2000,
                  easing: 'ease',
                  from: 1,
                  to: 0,
                  loop: undefined
                }
              },
              responsive:true,
              scales: {
                y: {
                  beginAtZero: true
                }
              }
            }
          });
  
        }    


        const myChartDoughnut1 = document.getElementById('myChartDoughnut1');
        if (myChartDoughnut1) {
          new Chart(myChartDoughnut1, {
            type: 'doughnut',
            data: {
              labels: [
                'Sold',
                'Stop'
              ],
              datasets: [{
                label: 'Orders',
                data: [57, 13],
                backgroundColor: [
                  'rgb(220, 53, 69)',
                  'rgb(25, 135, 84)'
                ],
                hoverOffset: 4
              }]
            },
            options: {
             
              responsive:true,
            
            }
          });
  
        }    

        const myChartDoughnut2 = document.getElementById('myChartDoughnut2');
        if (myChartDoughnut2) {
          new Chart(myChartDoughnut2, {
            type: 'doughnut',
            data: {
              labels: [
                'Act',
                'Out'
              ],
              datasets: [{
                label: 'Products',
                data: [12, 42],
                backgroundColor: [
                  
                 'rgb(220, 53, 69)',
                  'rgb(25, 135, 84)'
                ],
                hoverOffset: 2
              }]
            },
            options: {
             
              responsive:true,
            
            }
          });
  
        }    


        const myChartLineCustomers = document.getElementById('myChartLineCustomers');
        if (myChartLineCustomers) {
          new Chart(myChartLineCustomers, {
            type: 'line',
            data: {
              labels: ['01', '02', '03', '04', '05', '06','07'],
              datasets: [{
                label: 'login',
                data: [120,100,150,130, 49, 123,120],
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
        
        const myChartBarOrder = document.getElementById('myChartBarOrder');
        if (myChartBarOrder) {
          new Chart(myChartBarOrder, {
            type: 'bar',
            data: {
              labels: ['01', '02', '03', '04', '05', '06','07'],
              datasets: [{
                label: 'orders',
                data:  [50,102,330,80, 400,120,680],

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
          