import os
import re

# Precise labels from the user screenshot: About, Contact
footer_template = """    <footer class="cs_footer_style_1 cs_primary_bg cs_radius_16 position-relative overflow-hidden">
        <div class="container p-0">
            <!-- Newsletter -->
            <div class="cs_newsletter_style_1 cs_blue_bg1 cs_radius_16 position-relative z-1">
                <div class="cs_newsletter_text">
                    <h3 class="cs_fs_24 cs_white_color cs_mb_16 cs_primary_font">Join our local community</h3>
                    <p class="cs_white_color cs_primary_font mb-0">We occasionally send out special offers and helpful advice to help you keep your home looking its best.</p>
                </div>
                <form action="https://script.google.com/macros/s/AKfycbx-B1He7qGzZGq8HMQ2-ZsvfBU4dHyCaFBiQlowZCp_dmJd4xEFv03SSNg9smKfxOmi/exec" method="POST" class="cs_newsletter_form position-relative">
                    <input autocomplete="email" name="email" placeholder="Enter your email" required="" type="email" />
                    <button type="submit" class="cs_primary_font">Send</button>
                </form>
            </div>

            <div class="cs_footer_final_grid position-relative z-1">
                <!-- Col 1: Branding -->
                <div class="cs_footer_col">
                    <img alt="Logo" src="{ASSETS}img/logo-white.webp" style="width: 158px; margin-bottom: 25px;" />
                    <p class="cs_footer_desc">Bringing hotel-standard cleaning to Melbourne homes with a personal touch you can trust. Professional, reliable, and locally focused.</p>
                    <div class="cs_social_btns_style_1 mt-4">
                        <a href="https://www.facebook.com/profile.php?id=61573169063177" target="_blank"><img src="{ASSETS}img/icons/facebook-f-brands-solid-full.svg" width="20" height="20"></a>
                        <a href="https://www.instagram.com/maidathome_melb/" target="_blank"><img src="{ASSETS}img/icons/instagram-brands-solid-full.svg" width="20" height="20"></a>
                        <a href="https://wa.me/61413398546" target="_blank"><img src="{ASSETS}img/icons/whatsapp-brands-solid-full.svg" width="20" height="20"></a>
                    </div>
                </div>

                <!-- Col 2: Quick Links (EXACT MATCH TO HEADER IMAGE) -->
                <div class="cs_footer_col">
                    <h4 class="cs_footer_title">Quick Links</h4>
                    <ul class="cs_footer_link_list">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about-us">About</a></li>
                        <li><a href="/services">Services</a></li>
                        <li><a href="/pricing">Pricing</a></li>
                        <li><a href="/locations">Locations</a></li>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/faqs">FAQs</a></li>
                        <li><a href="/contact-us">Contact</a></li>
                    </ul>
                </div>

                <!-- Col 3: Our Services (Alphabetical) -->
                <div class="cs_footer_col">
                    <h4 class="cs_footer_title">Our Services</h4>
                    <ul class="cs_footer_link_list">
                        <li><a href="/services/deep-clean">Deep Spring Clean</a></li>
                        <li><a href="/services/move-in-out-clean">Move In/Out Clean</a></li>
                        <li><a href="/services/standard-clean">Standard House Clean</a></li>
                    </ul>
                </div>

                <!-- Col 4: Top Areas (Alphabetical) -->
                <div class="cs_footer_col">
                    <h4 class="cs_footer_title">Top Areas</h4>
                    <ul class="cs_footer_link_list cs_footer_list_with_icons">
                        <li><i class="fa-solid fa-location-dot"></i><a href="/locations/house-cleaning-albert-park">Albert Park</a></li>
                        <li><i class="fa-solid fa-location-dot"></i><a href="/locations/house-cleaning-melbourne-cbd">Melbourne CBD</a></li>
                        <li><i class="fa-solid fa-location-dot"></i><a href="/locations/house-cleaning-richmond">Richmond</a></li>
                        <li><i class="fa-solid fa-location-dot"></i><a href="/locations/house-cleaning-south-yarra">South Yarra</a></li>
                        <li><i class="fa-solid fa-location-dot"></i><a href="/locations/house-cleaning-toorak">Toorak</a></li>
                        <li><a href="/locations" style="color: var(--accent-color); font-weight: 700; margin-top: 5px;">+ See all 70+ areas</a></li>
                    </ul>
                </div>
            </div>

            <!-- Footer Bottom -->
            <div class="cs_footer_bottom position-relative z-1 py-4">
                <div class="cs_bottom_content d-flex justify-content-between align-items-center">
                    <div class="cs_copyright_text cs_fs_14 cs_gray_color2 cs_primary_font">
                        &copy; <span class="cs_getting_year">2026</span> Maid at Home. All rights reserved.
                    </div>
                    <ul class="cs_footer_bottom_menu cs_mp_0" style="list-style: none; display: flex; gap: 20px;">
                        <li><a href="/privacy-policy" class="cs_gray_color2 cs_fs_14 cs_primary_font">Privacy Policy</a></li>
                        <li><a href="/terms-conditions" class="cs_gray_color2 cs_fs_14 cs_primary_font">Terms & Conditions</a></li>
                    </ul>
                </div>
            </div>

            <!-- Vectors -->
            <div class="cs_vector_shape1 position-absolute"><img src="{ASSETS}img/vector-4.svg" /></div>
            <div class="cs_vector_shape2 position-absolute"><img src="{ASSETS}img/vector-5.svg" /></div>
        </div>
    </footer>"""

footer_pattern = re.compile(r'<!-- Start Footer Section -->.*?<!-- End Footer Section -->', re.DOTALL)

def process_file(filepath, is_suburb):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assets_path = "../assets/" if is_suburb else "assets/"
    new_footer = footer_template.replace("{ASSETS}", assets_path)
    new_content = footer_pattern.sub(f"<!-- Start Footer Section -->\n{new_footer}\n    <!-- End Footer Section -->", content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Execute
for file in os.listdir('.'):
    if file.endswith('.html'): process_file(file, False)
if os.path.exists('locations'):
    for file in os.listdir('locations'):
        if file.endswith('.html'): process_file(os.path.join('locations', file), True)

print("Final Polish Done.")
