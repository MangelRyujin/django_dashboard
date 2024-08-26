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
        