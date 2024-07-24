/* globals Chart:false */
const myChartBar = document.getElementById('myChartBar');
      if (myChartBar) {
        new Chart(myChartBar, {
          type: 'bar',
          data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
              label: '# of Votes',
              data: [120,100,150,130, 49, 123],
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
              labels: ['Red', 'Blue', 'Yellow', 'Green','Purple', 'Orange'],
              datasets: [{
                label: '# of Votes',
                data: [120,100,150,130, 49, 123],
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
        