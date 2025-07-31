# Fashion E-commerce Store

A modern, full-featured e-commerce platform built with Next.js, TypeScript, and Tailwind CSS. This project provides a complete online shopping experience similar to House of Prints, with features for fashion designs, ready-made clothing, and premium fabrics.

## 🚀 Features

### Core E-commerce Features
- **Product Catalog**: Browse and search through fashion items
- **Shopping Cart**: Add, remove, and manage cart items
- **User Authentication**: Secure sign-up/sign-in with NextAuth.js
- **Order Management**: Complete checkout and order tracking
- **Admin Panel**: Manage products, orders, and users
- **Payment Integration**: Stripe payment processing
- **Shipping Calculator**: UK-based shipping with multiple options

### User Experience
- **Responsive Design**: Mobile-first approach
- **Advanced Filtering**: Category, price range, and sorting
- **Wishlist**: Save favorite products
- **Product Reviews**: Customer ratings and feedback
- **Search Functionality**: Find products quickly
- **Real-time Updates**: Live cart and inventory updates

### Technical Features
- **TypeScript**: Full type safety
- **Prisma ORM**: Database management
- **PostgreSQL**: Robust database
- **Tailwind CSS**: Modern styling
- **Next.js 14**: App router and server components
- **Stripe**: Secure payment processing
- **NextAuth.js**: Authentication system

## 🛠️ Tech Stack

- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS
- **Backend**: Next.js API Routes, Prisma ORM
- **Database**: PostgreSQL
- **Authentication**: NextAuth.js
- **Payments**: Stripe
- **Styling**: Tailwind CSS, Radix UI
- **Deployment**: Vercel (recommended)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Node.js 18+ 
- npm or yarn
- PostgreSQL database
- Stripe account (for payments)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fashion-ecommerce
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Environment Setup
Copy the example environment file and configure your variables:

```bash
cp .env.example .env.local
```

Update `.env.local` with your configuration:

```env
# Database
DATABASE_URL="postgresql://username:password@localhost:5432/fashion_ecommerce"

# NextAuth.js
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-secret-key-here"

# Stripe
STRIPE_PUBLISHABLE_KEY="pk_test_your_stripe_publishable_key"
STRIPE_SECRET_KEY="sk_test_your_stripe_secret_key"
STRIPE_WEBHOOK_SECRET="whsec_your_webhook_secret"

# App Configuration
NEXT_PUBLIC_APP_URL="http://localhost:3000"
NEXT_PUBLIC_STORE_NAME="Fashion Store"
```

### 4. Database Setup
```bash
# Generate Prisma client
npx prisma generate

# Run database migrations
npx prisma migrate dev

# (Optional) Seed the database with sample data
npx prisma db seed
```

### 5. Start Development Server
```bash
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to see your application.

## 📁 Project Structure

```
fashion-ecommerce/
├── src/
│   ├── app/                    # Next.js app router
│   │   ├── api/               # API routes
│   │   ├── auth/              # Authentication pages
│   │   ├── products/          # Product pages
│   │   └── globals.css        # Global styles
│   ├── components/            # Reusable components
│   │   ├── ui/               # UI components
│   │   ├── layout/           # Layout components
│   │   └── providers/        # Context providers
│   ├── lib/                  # Utility functions
│   └── hooks/                # Custom hooks
├── prisma/                   # Database schema
├── public/                   # Static assets
└── package.json
```

## 🗄️ Database Schema

The application uses a comprehensive database schema with the following main entities:

- **Users**: Customer accounts and authentication
- **Products**: Product catalog with variants
- **Orders**: Order management and tracking
- **Cart**: Shopping cart functionality
- **Addresses**: Shipping and billing addresses
- **Reviews**: Product reviews and ratings
- **Categories**: Product categorization
- **Shipping**: Shipping zones and methods

## 🔧 Configuration

### Stripe Setup
1. Create a Stripe account
2. Get your API keys from the Stripe dashboard
3. Add them to your environment variables
4. Set up webhook endpoints for payment processing

### Database Configuration
1. Set up a PostgreSQL database
2. Update the DATABASE_URL in your environment variables
3. Run migrations to create the database schema

### Email Configuration (Optional)
For order notifications and password reset emails:

```env
EMAIL_SERVER_HOST="smtp.gmail.com"
EMAIL_SERVER_PORT=587
EMAIL_SERVER_USER="your-email@gmail.com"
EMAIL_SERVER_PASSWORD="your-app-password"
```

## 🚀 Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Add environment variables in Vercel dashboard
4. Deploy automatically

### Manual Deployment
1. Build the application: `npm run build`
2. Start the production server: `npm start`

## 📱 Features in Detail

### Product Management
- Product catalog with categories
- Product variants (size, color, etc.)
- Inventory management
- Product images and descriptions
- Pricing and discounts

### Shopping Experience
- Advanced product filtering
- Search functionality
- Wishlist management
- Shopping cart with persistence
- Guest checkout option

### Order Processing
- Secure checkout flow
- Multiple payment methods
- Order confirmation emails
- Order tracking
- Return/refund management

### User Management
- User registration and login
- Profile management
- Order history
- Address book
- Account settings

### Admin Features
- Product management
- Order management
- User management
- Analytics dashboard
- Inventory tracking

## 🔒 Security Features

- Password hashing with bcrypt
- JWT-based authentication
- CSRF protection
- Input validation and sanitization
- Secure payment processing
- Rate limiting on API routes

## 🧪 Testing

```bash
# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

## 📈 Performance

- Server-side rendering for SEO
- Image optimization
- Code splitting
- Lazy loading
- Caching strategies
- Database query optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation
- Review the code examples

## 🔄 Updates

To update the project:

```bash
# Update dependencies
npm update

# Update Prisma
npx prisma migrate dev

# Regenerate Prisma client
npx prisma generate
```

## 📊 Analytics

The application is ready for analytics integration:
- Google Analytics
- Facebook Pixel
- Custom event tracking
- Conversion tracking

## 🎨 Customization

### Styling
- Modify Tailwind CSS classes
- Update color scheme in `tailwind.config.js`
- Customize components in `src/components/ui/`

### Branding
- Update store name in environment variables
- Replace logo and favicon
- Customize email templates
- Update meta tags and SEO

### Features
- Add new product categories
- Implement additional payment methods
- Customize shipping rules
- Add loyalty program features

---

**Built with ❤️ using Next.js, TypeScript, and Tailwind CSS**
