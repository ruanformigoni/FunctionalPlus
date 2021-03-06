from conans import ConanFile, CMake

class FunctionalPlusConan(ConanFile):
    name = "functionalplus"
    version = "v0.2.8-p0"
    license = "Boost Software License 1.0"
    url = "https://github.com/Dobiasd/FunctionalPlus"
    description = "Functional Programming Library for C++. Write concise and readable C++ code."
    exports_sources = ["examples*", "cmake*", "include*", "CMakeLists.txt", "LICENSE"]
    options = {
        "build_unittest": [True, False],
    }
    default_options = "build_unittest=False",
    generators = ["cmake"]

    def requirements(self):
        if self.options.build_unittest:
            self.requires.add('doctest/2.3.4@bincrafters/stable')

    def package(self):
        # CMake
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
        # File copy
        self.copy("*LICENSE", dst="licenses")
        self.copy("*.hpp", src="include")
        self.copy("*.autogenerated_defines", src=".")
