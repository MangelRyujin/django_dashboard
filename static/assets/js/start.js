const allStart = document.querySelectorAll('.rating .star')
const rating = document.querySelector('.rating input')


allStart.forEach((item, idx)=>{
    item.addEventListener('click', function () {
        
        allStart.forEach(i=>{
            i.classList.replace('text-warning','text-body')
            rating.value = idx +1
            console.log(rating.value)
        })
        for(let i=0; i<allStart.length; i++){
            if(i<=idx){
                allStart[i].classList.replace('text-body','text-warning')
                rating.value = idx +1
            }
        }
    })
})