import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Header } from "@/components/layout/header"
import { ArrowRight, Star, ShoppingCart, Heart } from "lucide-react"

export default function HomePage() {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      
      {/* Hero Section */}
      <section className="relative h-[600px] bg-gradient-to-r from-purple-50 to-pink-50">
        <div className="container mx-auto px-4 h-full flex items-center">
          <div className="max-w-2xl">
            <h1 className="text-5xl font-bold text-gray-900 mb-6">
              Discover Your Style with
              <span className="text-primary block">Premium Fashion</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8">
              Explore our curated collection of fashion designs, ready-made clothing, 
              and premium fabrics. Quality meets style in every piece.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link href="/products">
                <Button size="lg" className="group">
                  Shop Now
                  <ArrowRight className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform" />
                </Button>
              </Link>
              <Link href="/categories">
                <Button variant="outline" size="lg">
                  Browse Categories
                </Button>
              </Link>
            </div>
          </div>
        </div>
        
        {/* Decorative Elements */}
        <div className="absolute top-20 right-20 w-32 h-32 bg-primary/10 rounded-full"></div>
        <div className="absolute bottom-20 right-40 w-24 h-24 bg-secondary/20 rounded-full"></div>
      </section>

      {/* Categories Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">Shop by Category</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {categories.map((category) => (
              <Link key={category.name} href={`/categories/${category.slug}`}>
                <div className="group relative overflow-hidden rounded-lg bg-gray-100 hover:shadow-lg transition-all duration-300">
                  <div className="aspect-square bg-gradient-to-br from-gray-200 to-gray-300 flex items-center justify-center">
                    <div className="text-center">
                      <div className="text-4xl mb-4">{category.icon}</div>
                      <h3 className="text-xl font-semibold text-gray-900">{category.name}</h3>
                      <p className="text-gray-600 mt-2">{category.description}</p>
                    </div>
                  </div>
                  <div className="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors duration-300"></div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <div className="flex justify-between items-center mb-12">
            <h2 className="text-3xl font-bold">Featured Products</h2>
            <Link href="/products">
              <Button variant="outline">
                View All Products
                <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            </Link>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {featuredProducts.map((product) => (
              <div key={product.id} className="group bg-white rounded-lg overflow-hidden shadow-sm hover:shadow-lg transition-shadow duration-300">
                <div className="aspect-square bg-gray-200 relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-br from-gray-300 to-gray-400 flex items-center justify-center">
                    <div className="text-6xl text-gray-500">👗</div>
                  </div>
                  <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <Button size="sm" variant="secondary" className="rounded-full p-2">
                      <Heart className="h-4 w-4" />
                    </Button>
                  </div>
                </div>
                
                <div className="p-4">
                  <h3 className="font-semibold text-gray-900 mb-2">{product.name}</h3>
                  <div className="flex items-center mb-2">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className={`h-4 w-4 ${i < product.rating ? 'fill-current' : 'fill-none'}`} />
                      ))}
                    </div>
                    <span className="text-sm text-gray-500 ml-2">({product.reviews})</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className="text-lg font-bold text-primary">£{product.price}</span>
                      {product.originalPrice && (
                        <span className="text-sm text-gray-500 line-through">£{product.originalPrice}</span>
                      )}
                    </div>
                    <Button size="sm" className="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                      <ShoppingCart className="h-4 w-4 mr-1" />
                      Add
                    </Button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">Why Choose Us</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {features.map((feature) => (
              <div key={feature.title} className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <div className="text-2xl">{feature.icon}</div>
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Newsletter Section */}
      <section className="py-16 bg-primary text-primary-foreground">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-4">Stay Updated</h2>
          <p className="text-lg mb-8 opacity-90">
            Subscribe to our newsletter for the latest fashion trends and exclusive offers.
          </p>
          <div className="max-w-md mx-auto flex gap-4">
            <input
              type="email"
              placeholder="Enter your email"
              className="flex-1 px-4 py-2 rounded-md text-gray-900 focus:outline-none focus:ring-2 focus:ring-white"
            />
            <Button variant="secondary">
              Subscribe
            </Button>
          </div>
        </div>
      </section>
    </div>
  )
}

const categories = [
  {
    name: "Ready-Made Clothing",
    slug: "ready-made",
    icon: "👕",
    description: "Stylish ready-to-wear pieces for every occasion"
  },
  {
    name: "Fashion Designs",
    slug: "designs",
    icon: "🎨",
    description: "Unique fashion designs and patterns"
  },
  {
    name: "Premium Fabrics",
    slug: "fabrics",
    icon: "🧵",
    description: "High-quality fabrics for your creations"
  }
]

const featuredProducts = [
  {
    id: 1,
    name: "Elegant Summer Dress",
    price: 89.99,
    originalPrice: 129.99,
    rating: 4,
    reviews: 24
  },
  {
    id: 2,
    name: "Classic White Shirt",
    price: 45.00,
    rating: 5,
    reviews: 18
  },
  {
    id: 3,
    name: "Premium Cotton Fabric",
    price: 29.99,
    rating: 4,
    reviews: 31
  },
  {
    id: 4,
    name: "Designer Pattern Set",
    price: 65.00,
    originalPrice: 85.00,
    rating: 4,
    reviews: 12
  }
]

const features = [
  {
    icon: "🚚",
    title: "Fast UK Delivery",
    description: "Free delivery on orders over £50. Next day delivery available."
  },
  {
    icon: "✨",
    title: "Premium Quality",
    description: "Carefully selected materials and expert craftsmanship."
  },
  {
    icon: "🔄",
    title: "Easy Returns",
    description: "30-day returns with no questions asked."
  }
]
