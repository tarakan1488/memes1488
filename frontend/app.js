const API_URL = 'https://memes1488-izrael.onrender.com'; // Замініть після деплою бекенду

// Завантаження при відкритті сторінки
document.addEventListener('DOMContentLoaded', () => {
    fetchMemes();
    fetchCategories();
});

// GET: Отримання мемів (з фільтрами)
async function fetchMemes() {
    const category = document.getElementById('categoryFilter').value;
    const sort = document.getElementById('sortFilter').value;
    
    let url = `${API_URL}/memes?sort_by=${sort}`;
    if (category) {
        url += `&category=${category}`;
    }

    try {
        const response = await fetch(url);
        const memes = await response.json();
        renderGallery(memes);
    } catch (error) {
        console.error("Помилка завантаження мемів:", error);
    }
}

// GET: Отримання категорій для селекта
async function fetchCategories() {
    try {
        const response = await fetch(`${API_URL}/categories`);
        const categories = await response.json();
        
        const filterSelect = document.getElementById('categoryFilter');
        filterSelect.innerHTML = '<option value="">Всі категорії</option>';
        
        categories.forEach(cat => {
            filterSelect.innerHTML += `<option value="${cat}">${cat}</option>`;
        });
    } catch (error) {
        console.error("Помилка завантаження категорій:", error);
    }
}

// Рендер карток мемів
function renderGallery(memes) {
    const gallery = document.getElementById('gallery');
    gallery.innerHTML = '';
    
    memes.forEach(meme => {
        const card = document.createElement('div');
        card.className = 'meme-card';
        
        const url = meme.image_url.toLowerCase();
        const isVideo = url.endsWith('.mp4') || url.endsWith('.webm');
        
        const mediaHTML = isVideo 
            ? `<video src="${meme.image_url}" autoplay loop muted playsinline onclick="openModal('${meme.image_url}', 'video')"></video>`
            : `<img src="${meme.image_url}" alt="${meme.title}" onclick="openModal('${meme.image_url}', 'img')">`;

        card.innerHTML = `
            <button class="delete-btn" onclick="deleteMeme(${meme.id})">×</button>
            ${mediaHTML}
            <div class="meme-info">
                <h3>${meme.title}</h3>
                <span class="category-tag">${meme.category}</span>
            </div>
        `;
        gallery.appendChild(card);
    });
}

// POST: Додавання мема
document.getElementById('addMemeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const newMeme = {
        title: document.getElementById('title').value,
        image_url: document.getElementById('imageUrl').value,
        category: document.getElementById('category').value
    };

    try {
        const response = await fetch(`${API_URL}/memes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newMeme)
        });

        if (response.ok) {
            document.getElementById('addMemeForm').reset();
            fetchMemes(); // Оновлюємо галерею
            fetchCategories(); // Оновлюємо список категорій
        }
    } catch (error) {
        console.error("Помилка створення мема:", error);
    }
});

function renderGallery(memes) {
    const gallery = document.getElementById('gallery');
    gallery.innerHTML = '';
    
    memes.forEach(meme => {
        const card = document.createElement('div');
        card.className = 'meme-card';
        
        const url = meme.image_url.toLowerCase();
        const isGif = url.includes('.gif');
        const isVideo = url.endsWith('.mp4') || url.endsWith('.webm');
        
        const gifBadgeHTML = (isGif || isVideo) ? `<span class="gif-badge">GIF</span>` : '';

        const mediaHTML = isVideo 
            ? `<video src="${meme.image_url}" autoplay loop muted playsinline></video>`
            : `<img src="${meme.image_url}" alt="${meme.title}">`;

        card.innerHTML = `
            ${gifBadgeHTML}
            <button class="delete-btn" onclick="deleteMeme(${meme.id})">×</button>
            ${mediaHTML}
            <div class="meme-info">
                <h3>${meme.title}</h3>
                <span class="category-tag">${meme.category}</span>
                <p style="font-size: 0.8rem; color: gray;">${new Date(meme.created_at).toLocaleDateString()}</p>
            </div>
        `;
        gallery.appendChild(card);
    });
}

// DELETE: Видалення мема
async function deleteMeme(id) {
    if(!confirm("Ви впевнені, що хочете видалити цей мем?")) return;

    try {
        await fetch(`${API_URL}/memes/${id}`, {
            method: 'DELETE'
        });
        fetchMemes(); // Оновлюємо галерею після видалення
    } catch (error) {
        console.error("Помилка видалення:", error);
    }
}

const modal = document.getElementById('imageModal');
const modalContent = document.getElementById('modalContent');

function openModal(src, type) {
    modal.style.display = "flex";
    if (type === 'video') {
        modalContent.innerHTML = `<video src="${src}" class="modal-content" autoplay loop controls></video>`;
    } else {
        modalContent.innerHTML = `<img src="${src}" class="modal-content">`;
    }
}

// Закрытие при клике на крестик
document.querySelector('.close-modal').onclick = () => {
    modal.style.display = "none";
    modalContent.innerHTML = ''; // Очищаем, чтобы видео перестало играть
};

// Закрытие при клике на темный фон
window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
        modalContent.innerHTML = '';
    }
};