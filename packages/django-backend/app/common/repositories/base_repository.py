NOT_IMPLEMENTED_ERROR_MESSAGE = 'You must define a `model` on the inheriting Repository'


class BaseRepository:
    model = None

    @classmethod
    def get(cls, *, pk):
        if not cls.model:
            raise NotImplementedError(NOT_IMPLEMENTED_ERROR_MESSAGE)

        try:
            instance = cls.model.objects.get(pk=pk)
        except cls.model.DoesNotExist:
            return None

        return instance

    @classmethod
    def get_queryset(cls, queryset=None):
        if queryset is None:
            if cls.model is None:
                raise NotImplementedError(NOT_IMPLEMENTED_ERROR_MESSAGE)

            return cls.model.objects.all()

        return queryset
