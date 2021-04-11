async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais')

    const animais = response.data

    const lista = document.getElementById('lista-animais')

    lista.innerHTML = ''

    animais.forEach(animal => {
        const item = document.createElement('li')

        const linha = `${animal.nome} - idade: ${animal.idade} - cor: ${animal.cor} - sexo: ${animal.sexo}`

        item.innerText = linha

        lista.appendChild(item)

        item.id = 'item'
        
    });

}


String.prototype.capitalize = function() {
	return this.charAt(0).toUpperCase() + this.substr(1);
}

function manipularFormulario() {
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')
    const input_idade = document.getElementById('idade')
    const input_cor = document.getElementById('cor')
    

    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value.capitalize()
        const idade_animal = input_idade.value
        const cor_animal = input_cor.value.capitalize()
        const sexo_animal = document.querySelector('input[name="opcao"]:checked').value
        

        await axios.post('http://localhost:8000/animais', {
            nome: nome_animal,
            idade: idade_animal,
            sexo: sexo_animal,
            cor: cor_animal
        })

        carregarAnimais()
        alert('Animal cadastrado..')
        document.querySelector('form').reset()
    }
}

function app() {
    console.log('App iniciada')
    carregarAnimais()
    manipularFormulario()
    capitalize()

}

app()