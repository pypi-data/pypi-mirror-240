from .Injector import Injector


def dependency_inject(*claDependencies):
    def classDecorator(cls):
        def decorator(*args, **kwargs):
            injector = Injector()
            objects = [
                injector.Get(claDependency) for claDependency in claDependencies
            ]

            return cls(*objects, *args, **kwargs)

        return decorator
    return classDecorator