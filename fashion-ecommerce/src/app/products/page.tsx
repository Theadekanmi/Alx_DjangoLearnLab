"use client"

import { useState } from "react"
import { Header } from "@/components/layout/header"
import { Button } from "@/components/ui/button"
import { Star, Filter, Grid, List, ShoppingCart, Heart } from "lucide-react"
import { formatPrice } from "@/lib/utils"

export default function ProductsPage() {
  const [viewMode, setViewMode] = useState<"grid" | "list">("grid")
  const [sortBy, setSortBy] = useState("featured")
  const [priceRange, setPriceRange] = useState([0, 500])
  const [selectedCategories, setSelectedCategories] = useState<string[]>([])

  const categories = [
    { id: "ready-made", name: "Ready-Made Clothing" },
    { id: "designs", name: "Fashion Designs" },
    { id: "fabrics", name: "Premium Fabrics" },
  ]

  const products = [
    {
      id: 1,
      name: "Elegant Summer Dress",
      price: 89.99,
      originalPrice: 129.99,
      rating: 4,
      reviews: 24,
      category: "ready-made",
      image: "👗",
      description: "A beautiful summer dress perfect for any occasion."
    },
    {
      id: 2,
      name: "Classic White Shirt",
      price: 45.00,
      rating: 5,
      reviews: 18,
      category: "ready-made",
      image: "👕",
      description: "Timeless white shirt for professional and casual wear."
    },
    {
      id: 3,
      name: "Premium Cotton Fabric",
      price: 29.99,
      rating: 4,
      reviews: 31,
      category: "fabrics",
      image: "🧵",
      description: "High-quality cotton fabric for your sewing projects."
    },
    {
      id: 4,
      name: "Designer Pattern Set",
      price: 65.00,
      originalPrice: 85.00,
      rating: 4,
      reviews: 12,
      category: "designs",
      image: "🎨",
      description: "Exclusive designer patterns for unique creations."
    },
    {
      id: 5,
      name: "Silk Evening Gown",
      price: 199.99,
      rating: 5,
      reviews: 8,
      category: "ready-made",
      image: "👗",
      description: "Luxurious silk evening gown for special occasions."
    },
    {
      id: 6,
      name: "Wool Blend Fabric",
      price: 39.99,
      rating: 4,
      reviews: 15,
      category: "fabrics",
      image: "🧵",
      description: "Warm and durable wool blend fabric."
    },
  ]

  const filteredProducts = products.filter(product => {
    const matchesCategory = selectedCategories.length === 0 || selectedCategories.includes(product.category)
    const matchesPrice = product.price >= priceRange[0] && product.price <= priceRange[1]
    return matchesCategory && matchesPrice
  })

  const sortedProducts = [...filteredProducts].sort((a, b) => {
    switch (sortBy) {
      case "price-low":
        return a.price - b.price
      case "price-high":
        return b.price - a.price
      case "rating":
        return b.rating - a.rating
      case "newest":
        return b.id - a.id
      default:
        return 0
    }
  })

  return (
    <div className="min-h-screen bg-background">
      <Header />
      
      <div className="container mx-auto px-4 py-8">
        {/* Page Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">All Products</h1>
          <p className="text-gray-600">Discover our collection of fashion items</p>
        </div>

        <div className="flex flex-col lg:flex-row gap-8">
          {/* Filters Sidebar */}
          <div className="lg:w-64 space-y-6">
            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="font-semibold mb-4 flex items-center">
                <Filter className="h-4 w-4 mr-2" />
                Filters
              </h3>

              {/* Categories */}
              <div className="mb-6">
                <h4 className="font-medium mb-3">Categories</h4>
                <div className="space-y-2">
                  {categories.map((category) => (
                    <label key={category.id} className="flex items-center">
                      <input
                        type="checkbox"
                        checked={selectedCategories.includes(category.id)}
                        onChange={(e) => {
                          if (e.target.checked) {
                            setSelectedCategories([...selectedCategories, category.id])
                          } else {
                            setSelectedCategories(selectedCategories.filter(id => id !== category.id))
                          }
                        }}
                        className="rounded border-gray-300 text-primary focus:ring-primary"
                      />
                      <span className="ml-2 text-sm">{category.name}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Price Range */}
              <div className="mb-6">
                <h4 className="font-medium mb-3">Price Range</h4>
                <div className="space-y-2">
                  <div className="flex justify-between text-sm">
                    <span>£{priceRange[0]}</span>
                    <span>£{priceRange[1]}</span>
                  </div>
                  <input
                    type="range"
                    min="0"
                    max="500"
                    value={priceRange[1]}
                    onChange={(e) => setPriceRange([priceRange[0], parseInt(e.target.value)])}
                    className="w-full"
                  />
                </div>
              </div>

              {/* Clear Filters */}
              <Button
                variant="outline"
                size="sm"
                onClick={() => {
                  setSelectedCategories([])
                  setPriceRange([0, 500])
                }}
                className="w-full"
              >
                Clear Filters
              </Button>
            </div>
          </div>

          {/* Products Grid */}
          <div className="flex-1">
            {/* Toolbar */}
            <div className="flex flex-col sm:flex-row justify-between items-center mb-6 bg-white p-4 rounded-lg shadow-sm">
              <div className="flex items-center space-x-4 mb-4 sm:mb-0">
                <span className="text-sm text-gray-600">
                  {sortedProducts.length} products
                </span>
                <select
                  value={sortBy}
                  onChange={(e) => setSortBy(e.target.value)}
                  className="text-sm border border-gray-300 rounded-md px-3 py-1 focus:outline-none focus:ring-2 focus:ring-primary"
                >
                  <option value="featured">Featured</option>
                  <option value="price-low">Price: Low to High</option>
                  <option value="price-high">Price: High to Low</option>
                  <option value="rating">Highest Rated</option>
                  <option value="newest">Newest</option>
                </select>
              </div>

              <div className="flex items-center space-x-2">
                <Button
                  variant={viewMode === "grid" ? "default" : "outline"}
                  size="sm"
                  onClick={() => setViewMode("grid")}
                >
                  <Grid className="h-4 w-4" />
                </Button>
                <Button
                  variant={viewMode === "list" ? "default" : "outline"}
                  size="sm"
                  onClick={() => setViewMode("list")}
                >
                  <List className="h-4 w-4" />
                </Button>
              </div>
            </div>

            {/* Products */}
            <div className={viewMode === "grid" 
              ? "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
              : "space-y-4"
            }>
              {sortedProducts.map((product) => (
                <div
                  key={product.id}
                  className={`bg-white rounded-lg overflow-hidden shadow-sm hover:shadow-lg transition-shadow duration-300 ${
                    viewMode === "list" ? "flex" : ""
                  }`}
                >
                  <div className={`${viewMode === "list" ? "w-48" : "aspect-square"} bg-gray-200 relative overflow-hidden`}>
                    <div className="absolute inset-0 bg-gradient-to-br from-gray-300 to-gray-400 flex items-center justify-center">
                      <div className="text-6xl text-gray-500">{product.image}</div>
                    </div>
                    <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                      <Button size="sm" variant="secondary" className="rounded-full p-2">
                        <Heart className="h-4 w-4" />
                      </Button>
                    </div>
                  </div>
                  
                  <div className={`p-4 ${viewMode === "list" ? "flex-1" : ""}`}>
                    <h3 className="font-semibold text-gray-900 mb-2">{product.name}</h3>
                    {viewMode === "list" && (
                      <p className="text-gray-600 text-sm mb-3">{product.description}</p>
                    )}
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
                        <span className="text-lg font-bold text-primary">{formatPrice(product.price)}</span>
                        {product.originalPrice && (
                          <span className="text-sm text-gray-500 line-through">{formatPrice(product.originalPrice)}</span>
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

            {sortedProducts.length === 0 && (
              <div className="text-center py-12">
                <p className="text-gray-500">No products found matching your criteria.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}