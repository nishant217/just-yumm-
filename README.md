# Just Yumm! - AI-Powered Recipe Assistant

Just Yumm! is a web-based recipe assistant that helps users discover, create, and explore recipes using AI technology. The platform provides personalized recipe recommendations, dietary planning, and cooking guidance.

Project Link: [https://just-yumm-2.onrender.com](https://just-yumm-2.onrender.com)

## Features

- **AI Recipe Chatbot**: Get instant recipe suggestions and cooking instructions
- **Dietary Planning**: Find recipes based on specific dietary restrictions
- **Ingredient-Based Search**: Discover recipes using available ingredients
- **Recipe Links**: Get reference links for specific dishes
- **User Authentication**: Create an account to save your chat history
- **Dark/Light Theme**: Choose your preferred interface theme
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **AI Integration**: Gemini API
- **Database**: SQLite
- **Styling**: Bootstrap, Boxicons
- **Fonts**: Poppins

## Project Structure

```
just-yum/
├── accounts/          # User authentication
├── base/             # Base templates
├── chatbot/          # Chatbot functionality
├── deit/             # Diet planning features
├── home/             # Home page
├── page1/            # Additional pages
├── products/         # Product management
├── public/           # Static files
├── templates/        # HTML templates
└── web/              # Project configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/just-yum.git
cd just-yum
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Usage

1. **Recipe Chat**:
   - Ask for recipe suggestions
   - Get detailed cooking instructions
   - Request recipe modifications

2. **Dietary Planning**:
   - Specify dietary restrictions
   - Get suitable recipe recommendations
   - Find alternative ingredients

3. **Ingredient Search**:
   - Enter available ingredients
   - Get recipe suggestions
   - Find creative ways to use ingredients

4. **Recipe Links**:
   - Search for specific dishes
   - Get reference links
   - Access external resources

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Boxicons](https://boxicons.com/)
- [Google Fonts](https://fonts.google.com/)

## Contact

Your Name - [Nishant Sharma](https://twitter.com/yourtwitter)

Project Link: [https://just-yumm-2.onrender.com](https://just-yumm-2.onrender.com)
