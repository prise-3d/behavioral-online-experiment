document.addEventListener('DOMContentLoaded',() => {
    
    // Do whatever you want
    const localStorage = window.localStorage;
    const sessionStorage = window.sessionStorage;

    // now check if new user, then add session id into local storage, if new id is generated
    const behavioral_user_id = localStorage.getItem('behavioral-experiment-user-id')

    // ask for new user id
    if (!sessionStorage.getItem('behavioral-experiment-user-id')) {

        getData('user/checkuser', 'POST', 'user_uuid', behavioral_user_id)
            .then(response => response.json())
            .then(data => {
                localStorage.setItem('behavioral-experiment-user-id', data[0]['pk'])
                sessionStorage.setItem('behavioral-experiment-user-id', data[0]['pk'])
            });
    }
});
